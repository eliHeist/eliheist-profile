from django.urls import path

from frontend.views import HomePageView

app_name = 'frontend'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]