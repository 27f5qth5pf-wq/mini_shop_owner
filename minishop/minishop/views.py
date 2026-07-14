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
    remove_new_line = request.GET.get('remove_new_line','off')
    
    functuations  = """`.,?!:;'"()[]}-{—…/\\|_@#$%&*+=^~``"""
    analyzed = ""

    for char in djtext:
        if removepunc == "on" and char in functuations:
            continue

        if remove_new_line == "on" and (char == "\n" or char == "\r"):
            continue

        if Upper_case == "on":
            analyzed += char.upper()
        else:
            analyzed += char
    
    params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
    return render(request,'analyzed.html',params)












    # if removepunc == "on":
    #     for char in djtext:
    #         if char not in functuations:
    #             analyzed = analyzed + char

    #     params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
    #     return render(request,'analyzed.html',params)

    # if Upper_case == "on":
    #     for char in djtext:
    #         if char not in functuations:
    #             analyzed = analyzed + char

    #     params = {'purpose': 'remove funchuation ','analyzed_text':analyzed.upper()}
    #     return render(request,'analyzed.html',params)

    # if remove_new_line == "on":
    #     for char in djtext:
    #         if char not in functuations:
    #             analyzed = analyzed + char

    #     params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
    #     return render(request,'analyzed.html',params)
        





    # # return HttpResponse(" Slide  page ")






# from django.http import HttpResponse
# from django.shortcuts import render

# def home (request):
#     # return render(request,'home.html')
#     onwer = {"name": "Afridi","address": "Karachi"}
#     return render(request,'home.html',onwer)

# def about (request):
#     return render(request,'about.html')

# def analyzes (request):
#     djtext = request.GET.get('text','default')
#     removepunc = request.GET.get('removepunc','off')
#     Upper_case = request.GET.get('Upper_case','off')
#     remove_new_line = request.GET.get('remove_new_line','off')
    
#     functuations  = """`.,?!:;'"()[]}-{—…/\\|_@#$%&*+=^~``"""
#     analyzed = ""

#     if removepunc == "on":
#         for char in djtext:
#             if char not in functuations:
#                 analyzed = analyzed + char

#         params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
#         return render(request,'analyzed.html',params)

#     if Upper_case == "on":
#         for char in djtext:
#             if char not in functuations:
#                 analyzed = analyzed + char

#         params = {'purpose': 'remove funchuation ','analyzed_text':analyzed.upper()}
#         return render(request,'analyzed.html',params)

#     if remove_new_line == "on":
#         for char in djtext:
#             if char not in functuations:
#                 analyzed = analyzed + char

#         params = {'purpose': 'remove funchuation ','analyzed_text':analyzed}
#         return render(request,'analyzed.html',params)
        





#     # return HttpResponse(" Slide  page ")
