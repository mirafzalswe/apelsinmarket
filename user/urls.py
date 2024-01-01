from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login-page'),
    path('logout/', views.Logout.as_view(), name='logout-page'),
    path('signup/', views.RegisterUser.as_view(), name='register-page'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('updateprofile/', views.EditProfileView.as_view(), name='setting-page'),
    path('myproducts/', views.my_products, name='my-product-page')
]
