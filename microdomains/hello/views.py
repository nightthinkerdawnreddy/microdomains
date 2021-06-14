from django.shortcuts import render 
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request,"home.html")
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        print(uploaded_file.name)
        print(uploaded_file.size)
        url=fs.url(uploaded_file)
        context={
            "url":url
        }
        return render(request,'download.html',context)    
    return render(request,'upload.html')
