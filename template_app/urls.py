from django.urls import path 
from . import views

app_name = 'myapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('services/', views.services, name='services'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
