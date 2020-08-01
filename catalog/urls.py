from django.urls import path
from .views import ProductListView, CategoryListView, product


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('produto/<slug:slug>/', product, name='product'),
]
