from django.urls import path



from .views import (CreateCartItemView,CartItemView,CheckoutView, 
                OrderListView, OrderDetailView, PagSeguroView,
                pagseguro_notification
                
                )


urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/',CreateCartItemView.as_view(),name='create_cart_item'),
    path('carrinho/',CartItemView.as_view(),name='cart_item_view'),
    path('carrinho/finalizar/',CheckoutView.as_view(),name='checkout_view'),
    path('meus-pedidos/',OrderListView.as_view(),name='order_list'),
    path('meus-pedidos/<int:pk>/',OrderDetailView.as_view(),name='order_detail'),
    path('finalizando/<int:pk>/pagseguro/',PagSeguroView.as_view(),name='pagseguro_view'),
    path('notificacoes/pagseguro/',pagseguro_notification,name='pagseguro_notification'),
    
]
