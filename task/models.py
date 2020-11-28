from django.db import models

class TODO(models.Model):

    title = models.CharField(max_length=300)
    added_date = models.DateTimeField()