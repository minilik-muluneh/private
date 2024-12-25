from django.shortcuts import render

# Create your views here.
def home(request,name='minilik',age=33):
    """ displaying the checkng html """
    return render(request,'checkings/index.html',{})