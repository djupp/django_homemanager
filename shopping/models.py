from django.db import models
from core.models import Good, Measurement


class Store(models.Model):

    name = models.CharField(max_length=30)


class Product(Good):

    store = models.ManyToManyField(Store, through="Purchase",
                                   through_fields=('what', 'where'))


class Purchase(models.Model):

    where = models.ForeignKey(Store)
    what = models.ForeignKey(Product)
    date = models.DateField()
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    unit = models.ForeignKey(Measurement)
    price = models.DecimalField(max_digits=6, decimal_places=2)
