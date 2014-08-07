from django.db import models


class Unit(models.Model):

    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=5, null=True, blank=True)
    baseUnit = models.ForeignKey("self", null=True)
    conversion = models.DecimalField(decimal_places=10, max_digits=20,
                                     default=1)

# For instance: "meter", blank, blank; "centimeter", "meter", .01; millimeter,
# meter, .001, foot, meter, .3248, ...

    def convert_to(self, other, amount):

        if self.baseUnit:
            # If this is a derived unit
            if self.baseUnit == other:
                # if the other unit is the matching base unit
                return round(amount * self.conversion, 3)
            elif other.baseUnit == self.baseUnit:
                # the other unit is also derived, and they match:
                return round(amount / other.conversion * self.conversion, 3)
            else:
                # they don't match
                return False
        else:
            if other.baseUnit == self:
                # this is the base unit for other
                return round(amount / other.conversion, 3)
            else:
                return False

    def list_related(self):
        if self.baseUnit:
            derivedUnits = Unit.objects.filter(baseUnit=self.baseUnit)
            return list(derivedUnits) + [self.baseUnit]
        else:
            derivedUnits = Unit.objects.filter(baseUnit=self)
            return list(derivedUnits) + [self]

    def __str__(self):
        if not self.baseUnit:
            return "%s (base unit)" % (self.name)
        else:
            return "%s <- %s" % (self.name, self.baseUnit.name)


class Good(models.Model):

    name = models.CharField(max_length=50)
    inStore = models.DecimalField(verbose_name="Amount of Good in Storage",
                                  max_digits=4, decimal_places=1)
    defaultUnit = models.ForeignKey(Unit, null=True)

    def modify(self, amount, unit):
        if unit.equals(self.defaultUnit):
            self.inStore += self.amount
        elif unit in self.defaultUnit.list_related():
            self.inStore += self.defaultUnit.convert_to(unit, amount)
