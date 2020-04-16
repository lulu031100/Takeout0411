from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import ShopCreateForm
from .models import Shop

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'takeout/shop_list.html'
    model = Shop

class AddView(generic.CreateView):
    template_name = 'takeout/shop_form.html'
    model = Shop
    form_class = ShopCreateForm
    success_url = reverse_lazy('takeout:index')
class UpdateView(generic.UpdateView):
    template_name = 'takeout/shop_form.html'
    model = Shop
    form_class = ShopCreateForm
    success_url = reverse_lazy('takeout:index')
class DeleteView(generic.DeleteView):
    template_name = 'takeout/shop_confirm_delete.html'
    model = Shop
    success_url = reverse_lazy('takeout:index')
class DetailView(generic.DetailView):
    template_name = 'takeout/shop_detail.html'
    model = Shop