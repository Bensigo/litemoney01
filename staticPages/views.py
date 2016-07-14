from django.shortcuts import render,redirect
from django.http import HttpResponse
from staticPages.forms import Contact
from django.template.loader import get_template
from django.template import context
from django.core.mail import send_mail,BadHeaderError
from django.conf import settings



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
	#importing settings so i use the EMAIL_HOST_USER
 	#getting ithe vale form the form
 	contact_email = request.POST.get('email','')
 	contact_title = request.POST.get('subject','')
 	contact_mail = request.POST.get('message','')
 	contact_name = request.POST.get('name','')
 	
 	if contact_name and contact_email and contact_title and contact_mail:
 		try:
 			#try and send the mail or else return an exception
 		    message = """
 				    from %s \n %s \n via %s

 			"""%(contact_name,contact_mail,contact_email)
 			#send the email
 		    send_mail(contact_title,contact_mail,contact_email,[settings.EMAIL_HOST_USER,],fail_silently=True)
 		    return redirect('contactComplete')	
 		except BadHeaderError:
 			return HttpResponse('invalid header error ')	
 	else:

 		template = 'staticTemplates/contact.html'
 		return render (request,template)

def contactComplete(request):
    return render (request,'staticTemplates/contactComplete.html')

# def contactUs(request):
# 	#render the contact us page and send email to comapny
# 	#importing settings so i use the EMAIL_HOST_USER
#  	#getting ithe vale form the form
#  	if request.method == 'POST':
#  		form = Contact(request.POST or None)
#  		if form.is_valid():
#  			contact_name = form.cleaned_data['Name']
#  			contact_email = form.cleaned_data['email']
#  			contact_title = form.cleaned_data['subject']
#  			contact_mail = form.cleaned_data['message']
#  			try:
#  			    #try and send the mail or else return an exception
#  			    message ="""
#  				    from %s \n %s \n via %s

#  			    """%(contact_name,contact_mail,contact_email)
#  			    #send the email
#  			    send_mail(contact_title,contact_mail,contact_email,[settings.EMAIL_HOST_USER,],fail_silently=True)
#  			    return redirect('contactComplete')	
#  			except BadHeaderError:
#  			    return HttpResponse('invalid header error ')
#  		else:
#  			form = Contact()
#  			context = {'form':form}
#  			template = 'staticTemplates/contact.html'
#  			return render (request,template,context)

#  	else:
#  		form = Contact
#  		context = {'form':form}
#  		template = 'staticTemplates/contact.html'
#  		return render (request,template,context)

