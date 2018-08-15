from django.db import models

class Prod(models.Model):
    item = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=4, decimal_places=2,)
