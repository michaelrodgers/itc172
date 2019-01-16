from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClubType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription = models.CharField(max_length=255)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'clubtype'

class ClubProduct(models.Model):
    productname = models.CharField(max_length=255)
    clubtype = models.ForeignKey(ClubType, on_delete=models.CASCADE)
    entryDate = models.DateField()
    productURL = models.URLField()
    productdescription = models.TextField()

    def __str__(self):
        return self.productname

    class Meta:
        db_table='clubproduct'
