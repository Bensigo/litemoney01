from django.conf.urls import url 
from . import views

urlpatterns =[

	      url(r'^$',views.news_list,name='news_list'),
	      url(r'^(?P<pk>[0-9]+)/$',views.news_details,name='news_details'),



]