from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import redirect


def root_redirect(request):
    # Редиректим только если нет языкового префикса
    if request.path.strip('/') == '':
        return redirect('/api/docs/', permanent=False)
    return redirect(request.path)


urlpatterns = [
    path('', lambda request: redirect('/api/docs/', permanent=False)),  # Swagger только на чистом "/"

    path('i18n/', include('django.conf.urls.i18n')),  # Переключение языка

    # API
    path('api/catalog/', include('catalog.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/leads/', include('leads.urls')),

    # Swagger/OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Админка и другие маршруты с поддержкой языка
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)
