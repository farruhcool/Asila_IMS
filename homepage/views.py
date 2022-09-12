from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

from inventory.models import Stock


class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        labels = []
        data = []
        stock_queryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stock_queryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = ['1']  # SaleBill.objects.order_by('-time')[:3]
        purchases = ['1']  # PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases
        }
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"
