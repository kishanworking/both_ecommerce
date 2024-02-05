from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.Remove_cart.as_view(), name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.Remove_cart_item.as_view() , name='remove_cart_item'),

    path('checkout/', views.checkout, name='checkout'),

]




