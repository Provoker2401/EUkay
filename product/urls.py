from django.urls import path
from .views import LatestProductList
from .views import ProductDetail

urlpatterns = [
    path('latest-products/', LatestProductList.as_view(), name='latest-products'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='products'),
]
