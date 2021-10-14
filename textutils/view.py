# I HAVE CREATED THIS FILE -- SKK
from django.http import HttpResponse
from django.shortcuts import render    # use for templates

# uses of pipes

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def analys(request):
    # get the text
    djtext = request.POST.get("text", "default")
    #check  checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinerm = request.POST.get('newlinerm', 'off')
    spacerm = request.POST.get('spacerm', 'off')
    charcount = request.POST.get('charcount', 'off')
    print(removepunc)
    print(djtext)

    # check which checkbox is on
    if removepunc == "on":
    # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            # print(char)
            if char not in punctuations:
                # print(char)
                analyzed = analyzed+char
        params = {'purpose':'Removed punctutation', 'analyzed_text': analyzed}
        djtext = analyzed

    # analys the text

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed =  analyzed + char.upper()
        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlinerm == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'remove newline ', 'analyzed_text': analyzed}
        djtext = analyzed

    if spacerm == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extrasapce remove ', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = djtext
        params = {'purpose': 'remove newline ', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc != "on" and fullcaps != "on" and newlinerm != "on" and spacerm != "on"):
        return HttpResponse("Please select any other operation and try again.")

    return render(request, 'analys.html',  params)





