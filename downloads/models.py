from django.db import models

# Create your models here.
class Download(models.Model):
    name = models.CharField(max_length=100)
    is_image = models.BooleanField(default=False)
    file = models.FileField(upload_to='downloads/')

    def __str__(self):
        return self.name