
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('conta/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('compras/', include(('checkout.urls','checkout'), namespace='checkout')),
]
