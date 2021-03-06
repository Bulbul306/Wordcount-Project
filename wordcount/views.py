from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def eggs(request):
    return HttpResponse("Eggs are Great")

def count(request):
    fulltext=request.GET['fulltext']
    wordcount=fulltext.split()
    wordcountdict={}
    for word in wordcount:
        if word in wordcountdict:
            wordcountdict[word]+=1
        else:
            wordcountdict[word] =1
    sortedwords=sorted(wordcountdict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordcount),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')
