import re
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
        "skills": [],
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
    return information
    # Extract name
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if lines:
        information["name"] = lines[0]
    # Common skills
    skill_list = ["Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Django", "Flask", "React"]
    # find skills in resume
    for skill in skill_list:
        if skill.lower() in text.lower():
            information["skills"].append(skill)
    # Extract education section
    education_keywords = ["education", "degree", "university", "college", "school"]
    # Extract experience section
    experience_keywords = ["experience", "work", "employment", "internship"]
    lines_lower = [line.lower() for line in lines]
    for index, line in enumerate(lines_lower):
        if any(keyword in line for keyword in education_keywords):
            information["education"] = lines[index: index + 6]
        if any(keyword in line for keyword in experience_keywords):
            information["experience"] = lines[index: index + 6]
    return information