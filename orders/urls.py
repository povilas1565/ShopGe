from django.urls import path
from .views import OrderCreateAPIView, OrderSetInProgressAPIView, OrderSetPaidAPIView, OrderCancelAPIView

urlpatterns = [
    path('', OrderCreateAPIView.as_view(), name='order-create'),
    path('admin/<uuid:pk>/set_in_progress/', OrderSetInProgressAPIView.as_view(), name='order-set-in-progress'),
    path('admin/<uuid:pk>/set_paid/', OrderSetPaidAPIView.as_view(), name='order-set-paid'),
    path('admin/<uuid:pk>/cancel/', OrderCancelAPIView.as_view(), name='order-cancel'),
]
