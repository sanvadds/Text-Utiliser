# I have created this file - Sanvad
from django.http import HttpResponse
from django.shortcuts import render

def home(request) :

    return render(request,'home.html')
    #return HttpResponse("Hello Sanvad <a href= 'https://www.youtube.com/watch?v=Mubj_fqiAv8&list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO' >Click Here</a>")

def about(request):
    return render(request,'about.html')

def contact(request) :
    details = {'name':'Sanvad B Shirke' , 'age':30 , 'mob' :7972806721 , 'place':'Kolhapur'}
    return render(request,'contact.html',details)

def analyzer(request) :
    djtext = request.POST.get('text','default')
    removepuc = request.POST.get('removepuc','off')
    capitalize = request.POST.get('capitalize','off')

    # this code of remove punctuation
    if removepuc == 'on' :
        analyzed_text = ""
        punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*~_'''
        for char in djtext :
            if char not in punctuations :
                analyzed_text = analyzed_text + char
        djtext = analyzed_text
        param = { 'analyzed_text' : analyzed_text}

    if capitalize == 'on' :
        analyzed_text = ""
        for char in djtext :
            analyzed_text = analyzed_text + str(char).upper()

        param = {'analyzed_text' : analyzed_text}

    if removepuc != 'on' and capitalize != 'on':
        return render(request,'error.html')

    return render(request, 'analyzer.html', param)