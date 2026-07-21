from .resume_parser import extract_resume_text, extract_resume_information
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
def home(request):
   if request.method == 'POST':
      resume = request.FILES.get('resume')
      if resume:
         fs = FileSystemStorage()
         filename = fs.save(resume.name, resume)
         file_path = fs.path(filename)
# Step 1: Extract text from the uploaded resume
         resume_text = extract_resume_text(file_path)
# Step 2: Extract information from the resume text
         resume_information = extract_resume_information(resume_text)
         return render(request, 'home.html', {
             'message': 'Resume analyzed successfully!',
             'resume_text': resume_text,
             'resume_information': resume_information
         })
         return render(request, 'home.html')