from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  photo = models.CharField(max_length=400, blank=True) # URL to the photo
  quantity = models.IntegerField()
  creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)