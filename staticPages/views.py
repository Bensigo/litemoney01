from django.shortcuts import render,redirect
from django.http import HttpResponse
from staticPages.forms import Contact
from django.template.loader import get_template
from django.template import context
from django.core.mail import send_mail,BadHeaderError



def FQAS(request):
	# display the FAQS(favorite que and ansers )
	template = 'staticTemplates/FQAS.html'
	return  render(request,template)

def about(request):
	#display our about page
	template = 'staticTemplates/about.html'
	return render (request,template)



def pricing(request):
	#show our pricing plan
	template = 'staticTemplates/pricing.html'
	return render (request,template)

def contactUs(request):
	#render the contact us page and send email to comapny
 	contact_email = request.POST.get('email','')
 	contact_title = request.POST.get('subject','')
 	contact_mail = request.POST.get('content','')
 	contact_name = request.POST.get('name','')
 	if contact_name and contact_email and contact_mail and contact_title:
 		try:
 			send_mail(contact_title,contact_name,contact_mail,contact_email,['info@litemoney.net'])
 		except BadHeaderError:
 				HttpResponse("invalid header found ")
 		return redirect('contact')

 	else:
 		HttpResponse('make sure all field enter is valid ')
