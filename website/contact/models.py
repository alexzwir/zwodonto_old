from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

#(name="Alex",email="alexzwir@gmail.com",phone="(11)98582-4810",subject="First Contact",message="First contact of many")
