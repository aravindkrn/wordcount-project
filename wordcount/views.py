from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'wordscount.html')

def helloWorld(request):
    return HttpResponse("<p><b>Hello World<b></p>")

def eggs(request):
    return render(request, 'eggs.html',{'name1':'Aravind', 'name2':'Krishnan'})

def count(request):
    usertext = request.GET['usertext']
    textlist = usertext.split()
    textlength = len(textlist)
    wordcount = {}
    for word in textlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    
    maxoccuredcount = max(wordcount.items(), key=operator.itemgetter(1))[1]
    maxoccured = [word for word in wordcount.items() if word[1] == maxoccuredcount]
    sortedwords = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)

    #print ("Text = {} \n Length = {} \n Max occured = {}".format(usertext, textlength, maxoccured))
    return render(request, 'count.html', {'text':usertext, 'count':textlength, 'maxoccured':maxoccured, 'wordcount':sortedwords})

def about(request):
    return render(request, 'about.html')