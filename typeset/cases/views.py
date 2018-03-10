from django.shortcuts import render
from .models import (Case, Block)
# from django.http import JsonResponse

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


# def casejson(request):
#     data = {
    
#     }

#     for case in Case.objects.all():
#         case_data ={
#             'name':case.name
#             'blocks':blocks.objects.filter(case=case)
#         }
#         data.append()

#     return JsonResponse(list(Case.objects.all().values()), safe=False)

def check(text, case):
    blocks = Block.objects.filter(case = case)
    skipchars = {" "}
    #chars = list(set(text))
    chars = []
    for line in text.split():
        for l in line:
            if l not in chars:
                chars.append(l)
            
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

def override(request):
    # cases = Case.objects.all()
    case = Case.objects.get(pk=request.POST['typesetCase'])
    case.dict = check(request.POST['typesetText'],case)
    case.caseprint = 'True'
    for object in case.dict:
        if object['print'] == "False":
            case.caseprint = "False"
    context = {'typesetText':request.POST['typesetText'], 'case':case, 'caseName':request.POST['typesetCase']}
    return render(request, 'cases/override.html',context)

def success_minchars(request):
    case = Case.objects.get(pk=request.POST['typesetCase'])
    case.dict = check(request.POST['typesetText'],case)
    blocks = Block.objects.filter(case = case)
    for object in case.dict:
        if object['print'] == "False":
            try:
                theBlock = blocks.get(character=object['char'])
                theBlock.count = object['input']
                theBlock.save()
            except:
                newBlock = blocks.create(case = case, character=object['char'], count = object['input'])
                newBlock.save()
                continue
    context = {'typesetText':request.POST['typesetText'], 'case':case, 'caseName':request.POST['typesetCase']}
    return render(request, 'cases/success_minchars.html',context)

