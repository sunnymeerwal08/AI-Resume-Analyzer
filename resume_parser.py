import os
from docx import Document
import PyPDF2

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    elif ext == ".docx":
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif ext == ".pdf":
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    return text

def extract_skills(text):
    skills = ["Python", "Java", "C++", "SQL", "JavaScript", "Cybersecurity", "Machine Learning"]
    found = []
    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)
    return found
