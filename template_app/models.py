from django.db import models

class Shop(models.Model):
    furniture_name = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField()
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='furniture', default='profile.png')
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.furniture_name
    
    
class Team(models.Model):
    full_name = models.CharField(max_length=60,blank=False, null=False)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='team', default='profile.png')
    
    def __str__(self):
        return self.full_name
    
class Testimonials(models.Model):
    customer_name = models.CharField(max_length=60, blank=False, null=False)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='testimonials', default='profile.png')
    message = models.TextField(max_length=1000, blank=False, null=False)
    
    def __str__(self):
        return self.customer_name
    
class Services(models.Model):
    title = models.CharField(max_length=80, blank=False, null=False)
    image = models.FileField(upload_to='services')
    description = models.TextField(max_length=250, blank=False, null=False)
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    auther = models.CharField(max_length=50, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs', default='profile.png')
    
    def __str__(self):
        return self.title
    
class Messages(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField()
    message = models.TextField(max_length=1000, blank=False, null=False)
    
    def __str__(self):
        return self.first_name
    
    
class ContactUs(models.Model):
    icon = models.CharField(max_length=1000)
    ways_to_find = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.ways_to_find
    
class Pages(models.Model):
    page = models.CharField(max_length=20,blank=False, null=False, unique=True)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100,blank=True, null=True)
    has_button = models.BooleanField(default=False)
    
    def __str__(self):
        return self.page
    
class ImageGrid(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='grid', default='profile.png')
    
    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    name = models.CharField( max_length=20)
    link = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    

# Create your models here.
