from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length = 50)
    project_description = models.TextField(max_length = 500)
    project_members = models.CharField(max_length = 500)
    github_url = models.URLField()
    livesite_url = models.URLField()

    def __str__(self):
        return self.project_name
