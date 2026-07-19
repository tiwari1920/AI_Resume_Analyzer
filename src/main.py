from analyzer.resume_parser import parse_resume
print("="*40)
print("         AI Resume Analyzer")
print("=" * 40)
resume_path = input("Enter Resume File Path: ")
print("Resume Path entered: ",resume_path)
candidate = parse_resume(resume_path)
if candidate:
    candidate.display()
else:
    print("Resume analysis could not be completed.")