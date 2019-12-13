from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    suppliers = models.ForeignKey('suppliers.Suppliers', on_delete=models.PROTECT)
    amount = models.IntegerField()
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name