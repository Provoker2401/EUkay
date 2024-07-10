from django.urls import path
from .views import LatestProductList
from .views import ProductDetail
from .views import CategoryDetail

from product import views

urlpatterns = [
    path('latest-products/', LatestProductList.as_view(), name='latest-products'),
    path('products/search/', views.search, name='search'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='products'),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),

]
