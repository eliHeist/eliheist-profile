from django.shortcuts import redirect, render

from django.views import View

from contact.forms import ContactForm

# Create your views here.
class ContactPageView(View):
    def get(self, request):
        context = {
            'form': ContactForm()
        }
        template_name = 'contact/contactpage.html'
        return render(request, template_name, context)
    
    def post(self, request):
        form = ContactForm(request.POST)
        form.sendMessage()
        return redirect('contact:contact-page')