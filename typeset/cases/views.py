from django.shortcuts import render
from .models import (Case, Block)

def input(request):
    return render(request, 'cases/input.html')

def results(request):
    cases = Case.objects.all()
    for case in cases:
        case.dict = check(request.POST['typesetText'],case)

    context = {'typesetText':request.POST['typesetText'], 'Cases':cases}
    return render(request, 'cases/results.html',context)


def check(text, case):
    blocks = Block.objects.filter(case = case)
    chars = list(set(text))
    chardict = {}
    for char in chars:
        try:
            count = blocks.get(character=char).count
            if(count):
                if (count < text.count(char)):
                    chardict[char] = [False,text.count(char)-count]
                if (count >= text.count(char)):
                    chardict[char] = [True,count-text.count(char)]
        except:
            chardict[char] = [False, "No such char"]

    return chardict
## Heat map
## Print out the five least char we have
## make the input field bigger
