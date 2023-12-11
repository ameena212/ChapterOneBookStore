from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', views.process_order, name='process_order'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('success_page/', views.success_page, name='success_page'),
]
