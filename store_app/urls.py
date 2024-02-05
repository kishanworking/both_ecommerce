
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views 

urlpatterns = [
    
    path('', views.Store.as_view(), name="store"),
    path('category/<slug:category_slug>/', views.Store.as_view() , name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.Product_detail.as_view() , name='product_detail'),
    path('search/',views.search, name='search')


]