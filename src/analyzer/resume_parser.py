from utils.file_handler import read_resume
from models.candidates import Candidate
def parse_resume(file_path):
    content = read_resume(file_path)
    if content is None:
        return None
    candidate = Candidate()
    for line in content.splitlines("\n"):
        if line.startswith("Name:"):
            candidate.name = line.replace("Name:","").strip()
        elif line.startswith("Email:"):
            candidate.email = line.replace("Email:","").strip()
        elif line.startswith("Phone:"):
            candidate.phone = line.replace("Phone:","").strip()
    return candidate