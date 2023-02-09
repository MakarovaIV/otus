from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView


def main_page(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "pokupka/index.html", context=context)


class ItemListView(ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["help_text"] = "Click on Item to get more information"
        return context


class ItemDetailView(DetailView):
    model = Item
