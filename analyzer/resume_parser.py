from pydoc import text
import re
from django.utils import text
import fitz 
from docx import Document
def extract_text_from_pdf(file_path):
    text = ""
    pdf = fitz.open(file_path)
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text
def extract_text_from_docx(file_path):
    document = Document(file_path)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text
def extract_resume_text(file_path):
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file format. Please upload a PDF or DOCX file."
def extract_resume_information(text):
    information = {
        "name": "",
        "email": "",
        "phone": "",
        "skills": {},
        "experience": [],
        "education": []
    }
    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if email_match:
        information["email"] = email_match.group()
    # Extract phone number
    phone_match = re.search(r'\+?\d[\d -]{8,12}\d', text)
    if phone_match:
        information["phone"] = phone_match.group()
    # Extract name
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if lines:
        information["name"] = lines[0]
   # Extract skills
    skill_categories = {
        "Programming Languages": [
            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript"
        ],

        "Web Technologies": [
            "HTML",
            "CSS",
            "JavaScript"
        ],

        "Frameworks": [
            "Django",
            "Flask",
            "React"
        ],

        "Databases": [
            "SQL",
            "MySQL",
            "PostgreSQL",
            "MongoDB"
        ],

        "Tools": [
            "Git",
            "GitHub",
            "VS Code"
        ]}

    # Convert resume text to lowercase
    resume_text_lower = text.lower()
    # Check each category
    for category, skills in skill_categories.items():
        # Create an empty list for this category
        information["skills"][category] = []
        # Check each skill
        for skill in skills:
            if skill.lower() in resume_text_lower:
                information["skills"][category].append(skill)
    # Extract education section
    education_keywords = ["education", "academic background", "qualifications", "degrees"]
    # Extract experience section
    experience_keywords = ["experience", "work experience", "professional experience", "employment history"]
    lines_lower = [line.lower() for line in lines]
    # Find education section
    for index, line in enumerate(lines_lower):
        if any(keyword == line.strip() for keyword in education_keywords):
            information["education"] = lines[index + 1:index + 6]
            break
    # find experience section
    for index, line in enumerate(lines_lower):
        if any(keyword in line for keyword in experience_keywords):
            information["experience"] = lines[index + 1:index + 6]
            break
    return information