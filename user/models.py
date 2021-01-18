from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    image=models.ImageField(upload_to="gallery/")


    def __str__(self):
        return self.name
