from django.db import models

from projects.models import Project

# Create your models here.
class HProject(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Hompage Project'
        verbose_name_plural = 'Hompage Projects'

    def __str__(self):
        return self.project.name
