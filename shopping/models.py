from django.db import models
from core.models import Good, Unit
from django.core.urlresolvers import reverse


class Store(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(Good):
    pass


class Purchase(models.Model):

    where = models.ForeignKey(Store)
    date = models.DateField()
    items = models.ManyToManyField(Product, through="PurchaseItem",
                                  through_fields=('purchase', 'product'))

    def get_absolute_url(self):
        return reverse('PurchaseDetail', kwargs={'pk': self.pk})

class PurchaseItem(models.Model):

    purchase = models.ForeignKey(Purchase)
    product = models.ForeignKey(Product)
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    unit = models.ForeignKey(Unit)
    price = models.DecimalField(max_digits=6, decimal_places=2)
