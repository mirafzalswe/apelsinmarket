from django.urls import path
from . import views
urlpatterns = [
    path('',views.ProductHome.as_view(), name='home-page'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='detail-page'),
    path('add/', views.CreateProduct.as_view(), name='add-product'),
    path('update/<int:pk>/', views.ProductUpdate.as_view(), name='update-product'),
    path('delete/<int:pk>/',  views.DeleteProudct.as_view(), name='delete-product'),
    path('search/', views.search_product, name='search-page')
]