from django.shortcuts import render,get_object_or_404
from .models import  News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def listing (request):
	news_list = News.objects.all().order_by('-pk')
	paginator = Paginator(news_list,10)#show ten news per page
	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		#if page not an interger,diviver firs page
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)
	context = {'news':news}
	template = 'newsTemplates/index.html'
	return render(request,template,context)




def news_details(request,pk):
	#show indivisual post
	news_detail = get_object_or_404(News,pk=pk)
	template = 'newsTemplates/news_details.html'
	context = {'news_detail':news_detail}
	return render (request,template,context)




