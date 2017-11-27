from django.shortcuts import render
from .models import (Case, Block)

def input(request):
    return render(request, 'cases/input.html')

def results(request):
    cases = Case.objects.all()
    for case in cases:
        case.dict = check(request.POST['typesetText'],case)
        case.caseprint = 'True'
        for object in case.dict:
            if object['print'] == "False":
                case.caseprint = "False"
    context = {'typesetText':request.POST['typesetText'], 'Cases':cases}
    return render(request, 'cases/results.html',context)


def check(text, case):
    blocks = Block.objects.filter(case = case)
    skipchars = {" "}
    specialchars = ['ff']
    #chars = list(set(text))
    chars = []
    for line in text.split():
        i = 0
        while i < (len(line)):
            # check for special characters, eg. ff
            if i<(len(line) -2):
                if (str(line[i]+line[i+1]) in specialchars):
                    special = str(line[i] + line[i+1])
                    if special not in chars:
                        chars.append(special)
                    i += 2
                    continue
            # do a general check for new non-special chars
            if line[i] not in chars:
                chars.append(line[i])
            i += 1
            
    alldict = []
    for char in chars:
        if (char in skipchars):
            continue
        try:
            count = blocks.get(character=char).count
            if(count):
                if (count < text.count(char)):
                    chardict = {}
                    chardict['case'] = case
                    chardict['char'] = char
                    chardict['print'] = 'False'
                    chardict['count'] = count-text.count(char)
                    chardict['input'] = text.count(char)
                    chardict['database'] = count
                    alldict.append(chardict)
                if (count >= text.count(char)):
                    chardict = {}
                    chardict['case'] = case
                    chardict['char'] = char
                    chardict['print'] = 'True'
                    chardict['count'] = count-text.count(char)
                    chardict['input'] = text.count(char)
                    chardict['database'] = count
                    alldict.append(chardict)

        except:
            chardict = {}
            chardict['case'] = case
            chardict['char'] = char
            chardict['print'] = 'False'
            chardict['count'] = 0
            chardict['input'] = text.count(char)
            chardict['database'] = 0
            alldict.append(chardict)

    return alldict
## Heat map
## Print out the five least char we have
## make the input field bigger
