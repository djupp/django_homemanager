# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.forms.fields import DateInput
from shopping.models import Purchase


class PurchaseCreate(CreateView):
    template_name = "shopping/new_purchase.html"
    model = Purchase
    fields = ['where', 'what', 'date', 'amount', 'unit', 'price']

    class Meta:
        widgets = {'date': DateInput(attrs={'class': 'datepicker'})}

class PurchaseList(ListView):
    pass

class PurchaseDetail(DetailView):
    pass
