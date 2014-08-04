from django.db import models


class Measurement(models.Model):

    name = models.CharField("Unit", max_length=30)
    compatibleUnit = models.ManyToManyField("self", through="Conversion",
                                            blank=True, symmetrical=False)

    def __str__(self):
        return '%s' % (self.name)

    def check_compatible_measurement(self):
        return self.conversion.objects.all()


class Conversion(models.Model):

    fromUnit = models.ForeignKey(Measurement, related_name='ConvertFromUnit')
    toUnit = models.ForeignKey(Measurement, related_name='ConvertIntoUnit')
    factor = models.DecimalField(max_digits=5, decimal_places=1,
                                 verbose_name="Conversion factor")

    def __str__(self):
        return '%s equals %s %s' % (self.one, self.factor, self.other)

    def convertFrom(self, amount):
        return amount * self.factor

    def convertTo(self, amount):
        return amount / self.factor


class Good(models.Model):

    name = models.CharField(max_length=50)
    inStore = models.DecimalField(verbose_name="Amount of Good in Storage",
                                  max_digits=4, decimal_places=1)
    defaultUnit = models.ForeignKey(Measurement, blank=True)

    def modify(self, amount, unit):
        if unit.equals(self.defaultUnit):
            self.inStore += self.amount
        elif unit in self.defaultUnit.check_compatible_measurement():
            self.inStore += self.defaultUnit.convertInto(amount, unit)
