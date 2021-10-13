# I HAVE CREATED THIS FILE -- SKK
from django.http import HttpResponse
from django.shortcuts import render # use for templates

# def index(reuest):
    # f = open("./hello.txt", "r")
    # t = f.readline()
    # print(f.readline())
    # print(f.readline())
    # # f.close()
    # with open('hello.txt') as f:
    #     lines = f.readlines()
    #     print("lines:", lines)

    # file1 = open(r'hello.txt', "r+", encoding='UTF-8')
    # d = file1.read()
    # # print(d)
#     return HttpResponse("<h1>Hello shashi</h1>"
#                         "<a href='hello.txt'>click me</a>")
#
# def about(reuest):
#     return HttpResponse('''<h1>about me</h1> <a href="https://stackoverflow.com/questions/59190153/display
#     -contents-of-a-text-file-in-django-template">django template</a>''')
#
# def bussiness(reuest):
#     return HttpResponse("<h3>business me</h3>")


# uses of pipes


def index(request):
    # params={'name': 'shashi', 'place':'bhopal'}
    return render(request, 'index.html')
    # return HttpResponse('''Home <a href="https://www.codewithharry.com/">COH</a>''')

def analys(request):
    # get the text
    djtext = request.GET.get("text", "default")
    # removepunc = request.GET.get('removepuc', 'off')
    # print(removepunc)
    print(djtext)
    # analyzed = djtext
    # punctuations='''/ [-[\]{}() * +?., ;:,"<>\\ ^ $ |  # \s]/g, "\\$&"'''
    # analyzed = ""
    # for char in djtext:
    #     if char is not punctuations:
    #         analyzed = analyzed + char
    # params = {'purpose':'Removed punctutation', 'analyzed_text': analyzed}
    # analys the text
    return HttpResponse("remove punch")
    # return render(request, 'analys.html', params)



# def capfirst(request):
#     return HttpResponse('''captalize first <a href="https://youtu.be/X0BdSYf-4U0">indian jharoka</a>''')
#
# def newlinerm(request):
#     return HttpResponse('''pace new line <a herf="https://youtu.be/5i9xJZE2Lh8"> video</a>''')
#
# def spacerm(request):
#     return HttpResponse("remove of space <a href='/'> back </a>")
#
# def charcount(request):
#     return HttpResponse('''count of character <a herf="https://www.codewithharry.com/https://www.codewithharry.com/">youtube</a>''')
#
# def strcount(request):
#     return HttpResponse("string counter <a href='/'>back</a>")
