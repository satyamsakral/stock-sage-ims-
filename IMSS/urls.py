from django.contrib import admin
from django.urls import path
from .views import  inventory_list,per_product, product_update , add_product , delete, update, dashboard
urlpatterns = [
    path("", inventory_list, name="inventory_list"),
    path("per_product_view/<int:pk>", per_product, name="per_product_view"),
    path("add_inventory/", add_product, name="inventory_add"),
    path("delete/<int:pk>", delete, name="delete_inventory"),
    path("update/<int:pk>", update, name="inventory_update"),
    path("dashboard/", dashboard, name="dashboard")

]
