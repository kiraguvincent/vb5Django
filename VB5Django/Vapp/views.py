from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'Index.html')

def images(request):
    return render(request,'Gallery.html')

def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
def collection(request):
    return render(request,'collection.html')