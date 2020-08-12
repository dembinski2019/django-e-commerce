from django.urls import path



from .views import CreateCartItemView,CartItemView,CheckoutView


urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/',CreateCartItemView.as_view(),name='create_cart_item'),
    path('carrinho/',CartItemView.as_view(),name='cart_item_view'),
    path('carrinho/finalizar',CheckoutView.as_view(),name='checkout_view'),
    
]
