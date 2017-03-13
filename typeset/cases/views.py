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
    skipchars = {" "}
    chars = list(set(text))
    alldict = []
    for char in chars:
        if (char in skipchars):
            continue
        try:
            count = blocks.get(character=char).count
            if(count):
                if (count < text.count(char)):
                    # chardict[char] = [False,text.count(char)-count]
                    chardict = {}
                    chardict['char'] = char
                    chardict['print'] = 'False'
                    chardict['count'] = text.count(char)-count
                    alldict.append(chardict)
                if (count >= text.count(char)):
                    # chardict[char] = [True,count-text.count(char)]
                    chardict = {}
                    chardict['char'] = char
                    chardict['print'] = 'True'
                    chardict['count'] = count-text.count(char)
                    alldict.append(chardict)

        except:
            # chardict[char] = [False, "No such char"]
            chardict = {}
            chardict['char'] = char
            chardict['print'] = 'None'
            chardict['count'] = 'No such char'
            alldict.append(chardict)

    return alldict
## Heat map
## Print out the five least char we have
## make the input field bigger
