from .resume_parser import extract_resume_text
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
def home(request):
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        if resume:
            fs = FileSystemStorage()
            filename = fs.save(resume.name, resume)
            file_path = fs.path(filename)
            resume_text = extract_resume_text(file_path)
            return render(request, 'home.html',{
        'message': 'Resume uploaded successfully!',
        'resume_text': resume_text,
            },
            )
    return render(request, 'home.html')
