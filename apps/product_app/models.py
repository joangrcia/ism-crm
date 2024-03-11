from django.db import models

# Create your models here.
class ProductTrading(models.Model):
    name = models.CharField(max_length=20)
    leverage = models.IntegerField(default=0)
    min_deposit = models.IntegerField(default=0)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)