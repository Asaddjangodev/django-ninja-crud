from http.client import responses

from ninja import NinjaAPI
from .schema import CategorySchema, ProductSchema
from ecommerce.inventory.models import Category, Product
from typing import List

api = NinjaAPI()

# @api.get("/home")
# def home(request):
#     return "Hello World!"


@api.post("/inventory/category")
def post_category(request, data: CategorySchema):
    qs = Category.objects.create(**data.dict())
    return {"name": qs.name}

@api.post("/inventory/product")
def post_product(request, data: ProductSchema):
    qs = Product.objects.create(**data.dict())
    return {"name": qs.name}

@api.get("inventory/category/all/", response=List[CategorySchema])
def get_category_list(request):
    qs = Category.objects.all()
    return qs

@api.get("/inventory/products/category/{category_slug}", response=List[ProductSchema])
def get_products_by_category(request, category_slug: str):
    qs = Product.objects.filter(category__slug=category_slug)
    return qs