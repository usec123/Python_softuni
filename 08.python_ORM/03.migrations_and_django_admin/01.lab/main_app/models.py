from django.db import models


# 1
class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, null=False, blank=False)
    supplier = models.CharField(max_length=150, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)

    # 2
    barcode = models.IntegerField(default=0)

    def __str__(self):
        return self.name
