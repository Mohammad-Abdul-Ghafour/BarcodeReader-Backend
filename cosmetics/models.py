from django.db import models

class Cosmetics(models.Model):
    name = models.CharField(max_length=255)
    barcodde = models.BigIntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=3)
    price = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.name
