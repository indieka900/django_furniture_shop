from django.urls import path 
from . import views

app_name = 'myapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('view/<id>/', views.viewItem, name='view-item'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    # path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('services/', views.services, name='services'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('checkout/<int:product_id>/', views.CheckOut, name='checkout'),
    path('payment-success/<int:product_id>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:product_id>/', views.paymentFailed, name='payment-failed'),
]
