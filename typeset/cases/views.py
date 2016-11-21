from django.shortcuts import render
from .models import (Case, Block)

def input(request):
    return render(request, 'cases/input.html')

def results(request):
    cases = Case.objects.all()
    for case in cases:
        if (check(request.POST['typesetText'],case)[0] == True):
            case.passed = True
            case.count = check(request.POST['typesetText'],case)[1]
        else:
            case.passed = False
            case.count = check(request.POST['typesetText'],case)[1]

    context = {'typesetText':request.POST['typesetText'], 'Cases':cases}
    return render(request, 'cases/results.html',context)


def check(text, case):
    blocks = Block.objects.filter(case = case)
    chars = list(set(text))
    for char in chars:
        try:
            count = blocks.get(character=char).count
        except:
            return [False,"No such char"]
        if (count < text.count(char)):
            return [False,text.count(char)-count]
    return [True,count-text.count(char)]
