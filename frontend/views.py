from django.shortcuts import render

from django.views import View

from frontend.models import HProject

# Create your views here.
class HomePageView(View):
    def get(self, request):
        context = {
            'projects': HProject.objects.all(),
        }
        template_name = 'frontend/homepage.html'
        return render(request, template_name, context)