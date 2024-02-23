from django.db import models

# Create your models here.
class Uploaded(models.Model):
    file = models.FileField(upload_to='uploaded_files')