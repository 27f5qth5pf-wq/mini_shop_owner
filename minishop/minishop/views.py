from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    # return render(request,'home.html')
    onwer = {"name": "Afridi","address": "Karachi"}
    return render(request,'home.html',onwer)

def about (request):
    return render(request,'about.html')

def analyzes (request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    Upper_case = request.GET.get('Upper_case','off')
    
    # analyzed = djtext
    functuations  = """`.,?!:;'"()[]}-{—…/\\|_@#$%&*+=^~``"""
    analyzed = ""

    if removepunc == "on":
        for char in djtext:
            if char not in functuations:
                analyzed = analyzed + char

        params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)

    elif Upper_case == "on":
        for char in djtext:
            if char not in functuations:
                analyzed = analyzed + char.upper

        params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)





    # return HttpResponse(" Slide  page ")
