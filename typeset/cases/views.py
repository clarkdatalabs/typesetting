from django.shortcuts import render
from .models import (Case, Block)

def input(request):
    return render(request, 'cases/input.html')

def results(request):
    cases = Case.objects.all()
    for case in cases:
        if (check(request.POST['typesetText'],case)):
            case.passed = True
        else:
            case.passed = False

    context = {'typesetText':request.POST['typesetText'], 'Cases':cases}
    return render(request, 'cases/results.html',context)


def check(text, case):
    blocks = Block.objects.filter(case = case)
    chars = list(set(text))
    for char in chars:
        try:
            count = blocks.get(character=char).count
        except:
            return False
        if (count < text.count(char)):
            return False
    return True
