# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def index(request):
#     return render(request,'index.html')
# def analyzed(request):
#     #Getting texts
#     djTexts=request.POST.get('text','default')
#
#     #check the checkbox value
#     removepunc=request.POST.get('removepunc','off')
#     fullcaps=request.POST.get('fullcaps','off')
#     newlineremover=request.POST.get('newlineremover','off')
#     extraspaceremover=request.POST.get('extraspaceremover','off')
#
#     analysis=""
#
#     #checking which checkbox is on
#     if removepunc=='on':
#         punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         for char in djTexts:
#             if char not in punctuations:
#                 analysis+=char
#         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analysis}
#         return render(request, 'analyze.html', params)
#
#     elif fullcaps=='on':
#         for char in djTexts:
#             analysis+=char.upper()
#         params = {'purpose': 'Change To Uppercase', 'analyzed_text': analysis}
#         return render(request, 'analyze.html', params)
#
#     elif newlineremover=='on':
#         for char in djTexts:
#             if char !='\n':
#                 analysis+=char
#         params = {'purpose': 'New Lines Removed', 'analyzed_text': analysis}
#         return render(request, 'analyze.html', params)
#
#     elif extraspaceremover=='on':
#         for index,char in enumerate(djTexts):
#             if not (djTexts[index] == " " and djTexts[index + 1] == " "):
#                 analysis = analysis + char
#         params = {'purpose': 'Extra Space Removed', 'analyzed_text': analysis}
#         return render(request, 'analyze.html', params)
#     else:
#         return HttpResponse("Error")
#
#
#
#
#
#
#
#
#
#
#
