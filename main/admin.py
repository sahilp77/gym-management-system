from django.contrib import admin
from . import models

class BannerAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'alt_text')
admin.site.register(models.Banners, BannerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(models.Services,ServiceAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','detail')
admin.site.register(models.Page,PageAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('quest', 'ans')
admin.site.register(models.Faq,FaqAdmin)


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email','detail', 'send_time')
admin.site.register(models.Enquiry, EnquiryAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(models.Gallery,GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text','image_tag')
admin.site.register(models.GalleryImage,GalleryImageAdmin)

class PricingAdmin(admin.ModelAdmin):
    list_editable = ('highlight_status','max_member')
    list_display = ('title', 'price','max_member' ,'highlight_status')
admin.site.register(models.Pricing, PricingAdmin)

class SubPricingAdmin(admin.ModelAdmin):
    list_display = ('detail', 'subplans')
    def subplans(self, obj):
        return ", ".join([sub.title for sub in obj.pricing.all()])
admin.site.register(models.SubPricing,SubPricingAdmin)

class PlanDiscountAdmin(admin.ModelAdmin):
    list_display = ('pricing', 'total_months', 'total_discount')
admin.site.register(models.PlanDiscount, PlanDiscountAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user','image_tag')
admin.site.register(models.Subscriber, SubscriberAdmin )

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user','plan')
admin.site.register(models.Subscription, SubscriptionAdmin )

class TrainerAdmin(admin.ModelAdmin):
    list_editable = ('is_active',)
    list_display = ('full_name','is_active','mobile','image_tag')
admin.site.register(models.Trainer, TrainerAdmin)