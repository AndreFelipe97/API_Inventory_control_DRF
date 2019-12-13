from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    suppliers = models.ForeignKey('suppliers.Suppliers', on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product