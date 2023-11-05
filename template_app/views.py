from django.shortcuts import render,redirect
from .models import Pages, Team, Company,Pages, Testimonials, Blog, ContactUs, Messages, ImageGrid, Services,Shop


def home(request):
    testmonials = Testimonials.objects.all().order_by('?')
    page = Pages.objects.get(page='Home')
    products = Shop.objects.all().order_by('?')[:3]
    blog = Blog.objects.all().order_by('?')[:3]
    services = Services.objects.all().order_by('?')[:4]
    context = {
        'nav':'home',
        'page':page,
        'testmonials':testmonials,
        'products':products,
        'blogs':blog,
        'services':services,
    }
    return render(request, 'index.html',context)

def about(request):
    testmonials = Testimonials.objects.all().order_by('?')
    services = Services.objects.all().order_by('?')[:4]
    team = Team.objects.all()
    page = Pages.objects.get(page='About')
    context = {
        'nav':'about',
        'testmonials':testmonials,
        'services':services,
        'teams':team,
        'page':page,
    }
    return render(request, 'about.html', context)

def contact(request):
    page = Pages.objects.get(page='Contact')
    contactus = ContactUs.objects.all()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages = Messages(first_name = fname, last_name= lname, email=email, message= message)
        messages.save()
        return redirect ('/')
    context = {
        'page':page,
        'nav':'contact',
        'contactus': contactus,
    }
    return render(request, 'contact.html',context)

def cart(request):
    page = Pages.objects.get(page='Cart')
    context = {
        'page':page,
        'nav':'cart'
    }
    return render(request, 'cart.html', context)

def services(request):
    products = Shop.objects.all().order_by('?')[:3]
    services = Services.objects.all().order_by('?')
    testmonials = Testimonials.objects.all().order_by('?')
    page = Pages.objects.get(page='Services')
    context = {
        'nav':'services',
        'products':products,
        'services':services,
        'testmonials':testmonials,
        'page':page,
    }
    return render(request, 'services.html', context)

def shop(request):
    products = Shop.objects.all().order_by('?')
    products1 = Shop.objects.all().order_by('?')
    page = Pages.objects.get(page='Shop')
    context = {
        'page':page,
        'products':products,
        'products1':products1,
        'nav':'shop'
    }
    return render(request, 'shop.html', context)

def blog(request):
    testmonials = Testimonials.objects.all().order_by('?')
    blog = Blog.objects.all().order_by('?')
    page = Pages.objects.get(page='Blog')
    context = {'nav':'blog','blogs':blog,'testmonials':testmonials,'page':page,}
    return render(request, 'blog.html', context)

def thankyou(request):
    return render(request, 'thankyou.html',{'nav':'thankyou'})

def checkout(request):
    context = {'nav':'chechout'}
    return render(request, 'checkout.html', context)


# Create your views here.
