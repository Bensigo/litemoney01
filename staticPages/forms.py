from django import forms

class Contact(forms.Form):
	Name = forms.CharField(max_length=150,required=True)
	email =forms.EmailField(required=True)
	subject = forms.CharField(max_length=200,required=True)
	message = forms.CharField(widget=forms.Textarea,required=True)


