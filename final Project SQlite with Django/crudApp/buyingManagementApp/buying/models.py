from django.db import models

# Create your models here.

class Buying(models.Model):
    buyId = models.CharField(max_length=100)
    itemName = models.CharField(max_length=300)
    itemPrice = models.CharField(max_length=200)
    totalQty = models.CharField(max_length=20)

    class Meta:
        db_table="buying"