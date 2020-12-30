from django.urls import path
from . import views
from django.contrib.auth import models
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('contact/', views.contact, name = 'contact'),
    path('register/', views.register, name = 'register'),
    path('products/', views.products, name = 'products'),
    path('cart/<int:cart_id>/', views.cart, name = 'cart'),
    path('beverages/<int:pr_id>', views.beverages, name = 'beverages'),
    path('faq/', views.faq, name = 'faq'),
    path('groceries/<int:pr_id>', views.groceries, name = 'groceries'),
    path('household/<int:pr_id>', views.household, name = 'household'),
    path('personalcare/<int:pr_id>', views.personalcare, name = 'personalcare'),
    path('about/', views.about, name = 'about'),
    path('packagedfoods/<int:pr_id>', views.packagedfoods, name = 'packagedfoods'),
    path('logout/', views.logout, name = 'logout')
]
