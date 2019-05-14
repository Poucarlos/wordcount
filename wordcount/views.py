from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
#anytime some is looking for a specific url the request is the parameter to the function
   return render(request,'home.html',{'hello':'this is new'})

def count(request):
	fulltext=request.GET['fulltext']
	wordlist=fulltext.split()
	worddictionary={}
	for word in wordlist:
		if word in worddictionary:
		 #increace
		  worddictionary[word]+=1
		else:
			#add to the dictionary
			worddictionary[word]=1
	sorted_words=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sorted':sorted_words})

def about(request):
	return render(request,'about.html')
