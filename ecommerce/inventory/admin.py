from django.contrib import admin
from . import models
from .models import Category, Product, Media
import nested_admin
# Register your models here.

admin.site.register(models.Media)
class MediaInline(nested_admin.NestedTabularInline):
    model = Media
    extra = 1

admin.site.register(models.Product)
class ProductInline(nested_admin.NestedTabularInline):
    model = Product
    extra = 1

admin.site.register(models.Category)
class CategoryAdmin(nested_admin.NestedTabularInline):
    inlines = [ProductInline]
