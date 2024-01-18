from django.shortcuts import render, redirect
from .models import Pages, Team, Company, Pages, Testimonials, Blog, ContactUs, Messages, ImageGrid, Services, Shop, SocialMedia
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

def CheckOut(request, product_id):

    product = Shop.objects.get(id=product_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': product.furniture_name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'product_id': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'product_id': product.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': product,
        'paypal': paypal_payment
    }

    return render(request, 'checkout.html', context)

def PaymentSuccessful(request, product_id):

    product = Shop.objects.get(id=product_id)

    return render(request, 'payment-success.html', {'product': product})

def paymentFailed(request, product_id):

    product = Shop.objects.get(id=product_id)

    return render(request, 'payment-failed.html', {'product': product})



#common to all pages
def common_data(pageName):
    return {
        'testmonials': Testimonials.objects.all().order_by('?'),
        'products' : Shop.objects.all().order_by('?')[:3],
        'pages': Pages.objects.all(),
        'media': SocialMedia.objects.all(),
        'company' : Company.objects.last(),
        'page': Pages.objects.get(page=pageName),
        'nav' : pageName.lower()
    }

def home(request):
    blog = Blog.objects.all().order_by('?')[:3]
    services = Services.objects.all().order_by('?')[:4]
    context = {
        'blogs': blog,
        'services': services,
        **common_data('Home'),
    }
    return render(request, 'index.html', context)

def about(request):
    services = Services.objects.all().order_by('?')[:4]
    team = Team.objects.all()
    context = {
        'services': services,
        'teams': team,
        **common_data('About'),
    }
    return render(request, 'about.html', context)

def contact(request):
    contactus = ContactUs.objects.all()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages = Messages(first_name=fname, last_name=lname, email=email, message=message)
        messages.save()
        return redirect('/')
    context = {
        'contactus': contactus,
        **common_data('Contact'),
    }
    return render(request, 'contact.html', context)

def blog(request):
    blog = Blog.objects.all().order_by('?')
    context = {
        'blogs':blog,
        **common_data('Blog'),
    }
    return render(request, 'blog.html', context)

def cart(request):
    context = {
        **common_data('Cart'),
        'nav':'cart'
    }
    return render(request, 'cart.html', context)

def services(request):
    services = Services.objects.all().order_by('?')
    context = {
        'services':services,
        **common_data('Services'),
        
    }
    return render(request, 'services.html', context)

def shop(request):
    products = Shop.objects.all().order_by('?')
    products1 = Shop.objects.all().order_by('?')
    context = {
        **common_data('Shop'),
        'product_s':products,
        'products1':products1,
    }
    return render(request, 'shop.html', context)

def viewItem(request, id):
    item = Shop.objects.get(id=id)
    return render(request, 'view_item.html',{'item':item,**common_data('View')})

def thankyou(request):
    return render(request, 'thankyou.html', {'nav': 'thankyou'})

def checkout(request):
    context = {'nav': 'chechout'}
    return render(request, 'checkout.html', context)
