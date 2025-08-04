from django.shortcuts import render
from .models import Category
# Create your views here.


def product_list(request):
    categories = Category.objects.all()
    return render(request, "product_list.html", {"categories": categories})