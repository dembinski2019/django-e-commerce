
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('conta/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('catalogo/', include(('catalog.urls', 'catalog'), namespace='catalog')),
    path('compras/', include(('checkout.urls','checkout'), namespace='checkout')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
