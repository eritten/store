from django.db import models
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to="images")
    date_release = models.DateTimeField(default=now)
    def __str__(self):
        return self.project_name
#    def get_absolute_url(self):
#        return reverse()
