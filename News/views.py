from django.shortcuts import render,get_object_or_404
from .models import  News

# Create your views here.

def news_list(request):
	#diplay all the news in the page
	template = 'newsTemplates/index.html'
	news = News.objects.all().order_by('pk')
	context = {'news':news}
	return render (request,template,context)


def news_details(request,pk):
	#show indivisual post
	news_detail = get_object_or_404(News,pk=pk)
	template = 'newsTemplates/news_details.html'
	context = {'news_detail':news_detail}
	return render (request,template,context)

def error404(request):
	return render (request,'404.html')

def error500(request):
	return render (request,'500.html')



