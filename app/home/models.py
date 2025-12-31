from django.db import models

# Create your models here.
class taskLists(models.Model):
    task_name = models.CharField(max_length=100, null=False, blank=False)
    task_description = models.TextField(max_length=100)
    task_time = models.TextField(null=True, blank=True)
    task_status = models.TextField(null=True, blank=True)