from django.shortcuts import render
from django.http import HttpResponse
from staticPages.forms import Contact
from django.template.loader import get_template
from django.template import context
from django.core.mail import EmailMessage,BadHeaderError



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
 			contact_email = request.POST.get('email','')
 			contact_title = request.POST.get('subject','')
 			contact_mail = request.POST.get('content','')
 			contact_name = request.POST.get('name','')

 			template = get_template('contact_template')
 			context =({
 				'contact_name':contact_name,
 				'contact_title':contact_title,
 				'contact_email':contact_email,
 				'contact_mail':contact_mail,
 				})
 			content = template.render(context)
 			email = EmailMessage(
 				'new contact form submission',
 				content,
 				'your comapny liteMoney',
 				['info@litemoney.net'],
 				headers = {'Reply-To':contact_email}
 				)
 			email.send()
 			return redirect('contact')
 		else:#if form is not valid
 			template = 'staticTemplates/contact.html'
 			return render (request,template)
 		    

 	else:

 		template = 'staticTemplates/contact.html'
 		return render (request,template)
