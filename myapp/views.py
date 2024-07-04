from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def test(request):
    return HttpResponse("hello this site for Django!")

def testPage(request):
    return render(request,"test.html")

# def index(request):
#     return render(request,"index.html")

# def singup(request):
#     if request.method== "post":''
#     else:
#         messages.error(request,"Bed request method !!")
#         return redirect("signuppage")