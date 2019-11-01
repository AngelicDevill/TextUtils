from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def analyzed(request):
    #Getting texts
    djTexts=request.POST.get('text','default')

    #check the checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    analysis = ""
    def allFour(insertedData):
        analysis=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for index,i in enumerate(insertedData):
            if i not in punctuations and i !='\n' and not (insertedData[index] == " " and djTexts[index + 1] == " "):
                analysis+=i.upper()
        param={'purpose':'Applied all functionality','analyzed_text':analysis}
        return render(request,'analyze.html',param)
    def removePunctuationNewLineExtraspace(insertedData):
        analysis=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for index, i in enumerate(insertedData):
            if i not in punctuations and i != '\n' and not (insertedData[index] == " " and djTexts[index + 1] == " "):
                analysis += i
        param = {'purpose': 'Applied NewLine-ExtraSpace-NewLine Remover', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def removePunctuationUpperExtraspace(insertedData):
        analysis=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for index, i in enumerate(insertedData):
            if i not in punctuations and not (insertedData[index] == " " and djTexts[index + 1] == " "):
                analysis += i.upper()
        param = {'purpose': 'Applied Punctuation-ExtraSpace Rmover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def removePunctuationNewLineUpper(insertedData):
        analysis=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in insertedData:
            if i not in punctuations and i != '\n':
                analysis += i.upper()
        param = {'purpose': 'Applied NewLine-Punctuation Remover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def newLineUpperExtraSpace(insertedData):
        analysis = ''
        for index, i in enumerate(insertedData):
            if i  (insertedData[index] == " " and djTexts[index + 1] == " ") and i != '\n':
                analysis += i.upper()
        param = {'purpose': 'Applied NewLine-ExtraSpace Remover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def newLineExtraSpace(insertedData):
        analysis = ''
        for index, i in enumerate(insertedData):
            if i(insertedData[index] == " " and djTexts[index + 1] == " ") and i != '\n':
                analysis += i
        param = {'purpose': 'Applied NewLine-ExtraSpace Remover', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def removePunctuationExtraSpace(insertedData):
        analysis = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for index, i in enumerate(insertedData):
            if i not in punctuations and not (insertedData[index] == " " and djTexts[index + 1] == " "):
                analysis += i
        param = {'purpose': 'Applied Punctuation-ExtraSpace Rmover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def extraspaceUpper(insertedData):
        analysis=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for index, i in enumerate(insertedData):
            if not(insertedData[index] == " " and djTexts[index + 1] == " "):
                analysis += i.upper()
        param = {'purpose': 'Applied ExtraSpace Remover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def removePunctuationUpper(insertedData):
        analysis=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for  i in insertedData:
            if i not in punctuations:
                analysis += i.upper()
        param = {'purpose': 'Applied Punctuation Remover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def upperNewLine(insertedData):
        analysis = ''

        for i in insertedData:
            if i !='\n':
                analysis += i.upper()
        param = {'purpose': 'Applied Punctuation-ExtraSpace Rmover and Uppercase Converted', 'analyzed_text': analysis}
        return render(request, 'analyze.html', param)
    def removePunctuation(insertedData):
        analysis = ""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in insertedData:
            if i not in punctuations:
                analysis+=i
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analysis}
        return render(request, 'analyze.html', params)
    def fullcapsFun(insertedData):
        analysis=""
        for char in insertedData:
            analysis+=char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analysis}
        return render(request, 'analyze.html', params)
    def newlineremoverFun(insertedData):
        analysis=''
        for char in insertedData:
            if char !='\n':
                analysis+=char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analysis}
        return render(request,'analyze.html',params)
    def extraspaceremoverFun(insertedData):

        for index,char in enumerate(insertedData):
            if not (insertedData[index] == " " and djTexts[index + 1] == " "):
                analysis = analysis + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analysis}
        return render(request,'analyze.html',params)

    #checking which checkbox is on
    if removepunc=='on'and fullcaps=='on' and extraspaceremover=='on' and newlineremover=='on':
        return allFour(djTexts)
    elif removepunc=='on' and extraspaceremover=='on' and newlineremover=='on':
        return removePunctuationNewLineExtraspace(djTexts)
    elif removepunc=='on'and fullcaps=='on' and extraspaceremover=='on':
        return removePunctuationUpperExtraspace(djTexts)
    elif removepunc=='on'and fullcaps=='on' and newlineremover=='on':
        return removePunctuationNewLineUpper(djTexts)
    elif fullcaps=='on' and extraspaceremover=='on' and newlineremover=='on':
        return newLineUpperExtraSpace(djTexts)
    elif extraspaceremover=='on' and newlineremover=='on':
        return newLineExtraSpace(djTexts)
    elif removepunc=='on' and extraspaceremover=='on':
        return removePunctuationExtraSpace(djTexts)
    elif fullcaps=='on' and extraspaceremover=='on':
        return extraspaceUpper(djTexts)
    elif removepunc=='on'and fullcaps=='on':
        return removePunctuationUpper(djTexts)
    elif fullcaps=='on' and newlineremover=='on':
        return upperNewLine(djTexts)
    elif removepunc=='on':
        return removePunctuation(djTexts)
    elif fullcaps=='on':
        return fullcapsFun(djTexts)
    elif newlineremover=='on':
        return newlineremoverFun(djTexts)
    elif extraspaceremover=='on':
        extraspaceremoverFun(djTexts)
    else:
        return HttpResponse("Error")












