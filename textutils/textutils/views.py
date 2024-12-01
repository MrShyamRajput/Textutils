from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'main.html')


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('Uppercase','off')
    lowercase=request.POST.get('Lowercase','off')
    newlineremove=request.POST.get('Remove_Empty_Lines','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    if removepunc=='on':
        punc='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=''
        for char in djtext:
            if char not in punc:
                analyzed+=char
        params={'purpose':"Remove Punctuations",'your_text':djtext,'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if uppercase=="on":
        analyzed=djtext.upper()
        params={'purpose':"Full Lowercase",'your_text':djtext,'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if lowercase=="on":
        analyzed=djtext.lower()
        params={'purpose':"Full Lowercase",'your_text':djtext,'analyzed_text':analyzed}
        print(analyzed)
        return render(request,"analyze.html",params)
    
    if newlineremove=="on":
        analyzed='\n'.join([line for line in djtext.split('\n') if line.strip()])
        params={'purpose':"Remove Empty Lines",'your_text':djtext,'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if extraspaceremover=='on':
        analyzed=' '.join(djtext.split())
        params={'purpose':"",'your_text':djtext,'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

