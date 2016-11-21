from django.shortcuts import render
from .models import (Case, Block)

def input(request):
    return render(request, 'cases/input.html')

def results(request):
    cases = Case.objects.all()
    for case in cases:
        case.dict = check(request.POST['typesetText'],case)
        # if (check(request.POST['typesetText'],case)[0] == True):
        #     case.passed = True
        #     case.dict = [1,2,3]
        #     case.count = check(request.POST['typesetText'],case)[1]
        # else:
        #     case.passed = False
        #     case.dict = [1,2,3]
        #     case.count = check(request.POST['typesetText'],case)[1]

    context = {'typesetText':request.POST['typesetText'], 'Cases':cases}
    return render(request, 'cases/results.html',context)


def check(text, case):
    blocks = Block.objects.filter(case = case)
    chars = list(set(text))
    chardict = {}
    for char in chars:
        try:
            count = blocks.get(character=char).count
        except:
            chardict[char] = [False, "No such char"]
        if(count):
            if (count < text.count(char)):
                chardict[char] = [False,text.count(char)-count]
            if (count >= text.count(char)):
                chardict[char] = [True,count-text.count(char)]
    return chardict
