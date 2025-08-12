from django.urls import path
from .views import CartAPIView, CartItemCreateAPIView, CartItemUpdateAPIView, CartItemDeleteAPIView

urlpatterns = [
    path('', CartAPIView.as_view(), name='cart-detail'),
    path('items/', CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('items/<int:pk>/', CartItemUpdateAPIView.as_view(), name='cartitem-update'),
    path('items/<int:pk>/delete/', CartItemDeleteAPIView.as_view(), name='cartitem-delete'),
]
