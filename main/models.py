from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)
    
    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" style="width:80px;" />' % (self.img.url))



# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img =   models.ImageField(upload_to="services/", null = True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" style="width:80px;" />' % (self.img.url))
    

class Page(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Faq(models.Model):
    quest = models.TextField()
    ans = models.TextField()
    
    def __str__(self):
        return f"{self.quest[:50]}... {self.ans[:50]}..."
    
    
class Enquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    detail = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    
class Gallery(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    img =   models.ImageField(upload_to="gallery/", null = True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" style="width:80px;" />' % (self.img.url))
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    alt_text = models.CharField(max_length=150)
    img =   models.ImageField(upload_to="gallery_images/", null = True)
    
    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:80px;" />' % (self.img.url))
    
class Pricing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    max_member = models.IntegerField(null=True)
    highlight_status = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.title
    

class SubPricing(models.Model):
    # pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True)
    pricing = models.ManyToManyField(Pricing, related_name='subpricing_set')
    detail = models.TextField()
    
    def __str__(self):
        return self.detail
    
    
class PlanDiscount(models.Model):
    pricing=models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True)
    total_months = models.IntegerField()
    total_discount = models.IntegerField()
    
    def __str__(self):
        return self.total_months
    
    
class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile = models.IntegerField()
    address = models.TextField(max_length=150)
    img = models.ImageField(upload_to="subs/")

    def __str__(self):
        return self.user
    
    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" style="width:80px;" />' % (self.img.url))
        else:
            return 'No Image'


@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwargs):
    if created:
        subs= Subscriber.objects.create(user=instance)
        print(subs)
        


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
