from django.shortcuts import render,get_object_or_404
from .models import  News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def news_list(request):
	#diplay all the news in the page
	template = 'newsTemplates/index.html'
	news_list = News.objects.all().order_by('-pk')
	paginator = Paginator(contact_list, 10) # Show 10 news per page
	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page ...
        news = paginator.page(1)
    except EmptyPage:
    	news = paginator.page(paginator.num_pages)
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



