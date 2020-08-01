from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic



class ProductListView(generic.ListView):
    
    model=Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3


class CategoryListView(generic.ListView):
    
    template_name = 'catalog/category.html'
    context_object_name = 'products_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug = self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_category"] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context 
    



def product(request,slug):
    template = 'catalog/product.html'
    products = Product.objects.get(slug=slug)
    context = {
        'product': products,
    }
    return render(request,template, context)