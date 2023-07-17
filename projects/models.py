from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to=f'projects/')
    description = models.CharField(max_length=100)
    details = models.TextField()
    technologies = models.ManyToManyField('Technology', related_name='projects', blank=True)
    is_active = models.BooleanField(default=True)

    github_link = models.URLField(null=True, blank=True)
    live_link = models.URLField(null=True, blank=True)

    registered = models.DateTimeField(auto_now_add=True) 
    modified = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute url for Project."""
        return ('')

    # TODO: Define custom methods here

class Technology(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute url for Technology."""
        return ('')

    # TODO: Define custom methods here
