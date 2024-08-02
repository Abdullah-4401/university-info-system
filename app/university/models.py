from django.db import models

# Create your models here.
class UniData(models.Model):
    web_pages=models.JSONField()
    country=models.CharField(max_length=50)
    state_province=models.CharField(max_length=50,null=True,blank=True)
    domains=models.JSONField()
    alpha_two_code=models.CharField(max_length=2)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
