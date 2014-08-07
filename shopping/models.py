from django.db import models
from core.models import Good, Unit


class Store(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)


class Product(Good):

    store = models.ManyToManyField(Store, through="Purchase",
                                   through_fields=('what', 'where'))


class Purchase(models.Model):

    where = models.ForeignKey(Store)
    what = models.ForeignKey(Product)
    date = models.DateField()
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    unit = models.ForeignKey(Unit)
    price = models.DecimalField(max_digits=6, decimal_places=2)
