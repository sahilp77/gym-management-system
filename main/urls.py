from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from gymManageSys.settings import LOGOUT_REDIRECT_URL


urlpatterns = [
    path('',views.home, name='home'),
    path('pagedetail/<str:id>',views.page_detail, name='pagedetail'),
    path('faq/',views.faq, name='faq'),
    path('enquiry/',views.enquiry, name='enquiry'),
    path('gallery/',views.gallery, name='gallery'),
    path('galleryimage/<str:id>',views.galleryimage, name='galleryimage'),
    path('pricing/',views.pricing, name='pricing'),
    path('account/signup/', views.signup , name='signup'),
    path('account/logout/', auth_views.LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path('checkout/<str:plan_id>',views.checkout, name='checkout'),
    path('checkout_session/<str:plan_id>',views.checkout_session, name='checkout_session'),
    path('success/',views.success, name='success'),
    path('cancel/',views.cancel, name='cancel'),
    path('user-dashboard/',views.user_dashboard, name='user_dashboard'),
    path('update-profile/',views.update_profile, name='update_profile'),
    path('change-password/', views.change_password, name='new_password'),
    path('trainerlogin/', views.trainerlogin, name='trainerlogin'),
    path('trainerlogout/', views.trainerlogout, name='trainerlogout'),
    
    








]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)