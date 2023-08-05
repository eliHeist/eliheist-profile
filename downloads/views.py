from django.shortcuts import render
from django.urls.base import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from downloads.models import Download

# Create your views here.
class DownloadListView(ListView):
    template_name = 'downloads/download-list.html'
    model = Download
    context_object_name = 'downloads'

class DownloadCreateView(CreateView):
    template_name = 'downloads/download-create.html'
    model = Download
    fields = '__all__'
    success_url = 'downloads:list'

class DownloadUpdateView(UpdateView):
    template_name = 'downloads/download-update.html'
    model = Download
    fields = '__all__'
    success_url = 'downloads:list'

class DownloadDeleteView(DeleteView):
    template_name = 'downloads/download-delete.html'
    model = Download
    fields = '__all__'
