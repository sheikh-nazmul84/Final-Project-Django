from django.db import models

# Create your models here.

class Buying(models.Model):
    srNo = models.CharField(max_length=100)
    itemName = models.CharField(max_length=200)
    itemPrice = models.CharField(max_length=300)
    totalQty = models.CharField(max_length=200)


    class Meta:
        db_table="buying"