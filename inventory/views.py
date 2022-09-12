from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, View
from django_filters.views import FilterView

from .filters import StockFilter
from .forms import StockForm
from .models import Stock


class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'edit_stock.html'
    success_url = '/inventory'
    success_message = 'Maxsulot muvofaqiyatli yaratildi'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Yangi maxsulot'
        context["savebtn"] = 'Omborga qo\'shish'
        return context


class StockUpdateView(SuccessMessageMixin, UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'edit_stock.html'
    success_url = '/inventory'
    success_message = 'Maxsulot muvofaqiyatli yangilandi'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Maxsulot tahrirlash'
        context["savebtn"] = 'Maxsulotni yangilash'
        context["delbtn"] = 'Maxsulotni o\'chirish'
        return context


class StockDeleteView(View):
    template_name = 'delete_stock.html'
    success_message = 'Maxsulot muvofaqiyatli o\'chirildi'

    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object': stock})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()
        messages.success(request, self.success_message)
        return redirect('inventory')
