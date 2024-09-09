from django.db import models

# Create your models here.
class pagevisits(models.Model):
    page= models.TextField(null=True,blank=True)
    visit_time= models.DateTimeField(auto_now_add=True)