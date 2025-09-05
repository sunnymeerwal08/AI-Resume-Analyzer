from flask import Flask, render_template, request
import os
import pandas as pd
from recommender import recommend_jobs
from resume_parser import extract_text_from_file, extract_skills   # ✅ updated import

app = Flask(__name__)

# Load sample jobs
jobs = pd.read_csv("sample_jobs.csv")

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    recommended_jobs = []
    if request.method == "POST":
        if "resume" not in request.files:
            return "No file uploaded", 400
        file = request.files["resume"]
        if file.filename == "":
            return "No selected file", 400

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # ✅ Extract text & skills from uploaded resume
        resume_text = extract_text_from_file(filepath)
        skills = extract_skills(resume_text)

        # ✅ Recommend jobs based on extracted skills
        recommended_jobs = recommend_jobs(jobs, skills)

    return render_template("index.html", jobs=recommended_jobs)

if __name__ == "__main__":
    app.run(debug=True)
