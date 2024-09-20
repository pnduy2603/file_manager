from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.TextField(null=True)
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.CharField(max_length=10, blank=True, null=True)


