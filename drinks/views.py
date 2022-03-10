from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Drink


class DrinkListView(ListView):
    template_name = "drinks/drink_list.html"
    model = Drink


class DrinkDetailView(DetailView):
    template_name = "drinks/drink_detail.html"
    model = Drink


class DrinkCreateView(CreateView):
    template_name = "drinks/drink_create.html"
    model = Drink
    fields = ['name', 'description', 'purchaser']


class DrinkUpdateView(UpdateView):
    template_name = "drinks/drink_update.html"
    model = Drink
    fields = ['name', 'description', 'purchaser']


class DrinkDeleteView(DeleteView):
    template_name = "drinks/drink_delete.html"
    model = Drink
    success_url = reverse_lazy("drink_list")