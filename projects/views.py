from django.shortcuts import render
from django.views.generic import ListView, DetailView
from projects.models import Project

# Create your views here.

class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = "projects/project-list.html"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = "projects/project-detail.html"
