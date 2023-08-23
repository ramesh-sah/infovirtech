from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(("@"), max_length=254)
    phone=models.CharField(max_length=17)
    subject=models.CharField(max_length=255)
    msg=models.CharField(max_length=255)
