from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    CHOICES = (
        ('Other','Other'),
        ('Web Applications','Web Applications'),
        ('Software Development','Software Development'),
        ('Graphics Design','Graphics Design'),
        ('Music Production','Music Production'),
    )
    name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=50, required=True)
    cartegory = forms.ChoiceField(choices=CHOICES, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    # TODO attachments = forms.FileField(required=False)
    
    def sendMessage(self):
        message = f'''{self.message}\n\n{self.email}'''
        send_mail(f'{self.subject}: {self.cartegory}', message, 'test.eliheist@gmail.com', ['eliyang256@gmail.com',])
