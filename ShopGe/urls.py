from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', lambda request: redirect('swagger-ui', permanent=False)),  # 🚀 Редирект на Swagger

    # Языковой переключатель
    path('i18n/', include('django.conf.urls.i18n')),

    # Подключаем API из приложений
    path('api/catalog/', include('catalog.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/leads/', include('leads.urls')),

    # Swagger/OpenAPI схема и Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

# Админку оборачиваем в i18n_patterns, чтобы язык менялся
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

