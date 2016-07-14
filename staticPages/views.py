from django.shortcuts import render
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
 	form = Contact()
 	if request.method == "POST":
 		if form.is_valid():
 			#getting ithe vale form the form
 			contact_email = request.POST.get('email','')
 			contact_title = request.POST.get('subject','')
 			contact_mail = request.POST.get('content','')
 			contact_name = request.POST.get('name','')
 			message = """
 					from %s \n %s \n via %s

 			"""%(contact_name,contact_mail,contact_email)
 			#send the email
 			send_mail(contact_title,contact_mail,contact_email,['info@litemoney.net'],fail_silently=True)
 			return redirect('contact')
 		else:#if form is not valid
 			template = 'staticTemplates/contact.html'
 			return render (request,template)
 		    

 	else:

 		template = 'staticTemplates/contact.html'
 		return render (request,template)
