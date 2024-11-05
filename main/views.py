from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth import logout
import stripe
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# home page

def home(request):
    galleryimages = models.GalleryImage.objects.all().order_by()[:9]
    banners = models.Banners.objects.all()
    services = models.Services.objects.all()
    context = {"banners": banners, "services": services, 'galleryimages': galleryimages}
    return render(request, 'home.html', context)

def page_detail(request,id):
    page = models.Page.objects.get(id=id)
    context = {"page" : page}
    return render(request, 'page.html', context)


def faq(request):
    faqs = models.Faq.objects.all()
    context = {"faqs" : faqs}
    return render(request, 'faq.html', context)

def enquiry(request):
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            alert = "Enquiry submitted successfully!"
            return redirect("home")
    form = forms.EnquiryForm()
    context = {"form" : form,}
    return render(request, 'enquiry.html', context)

def gallery(request):
    gallerys = models.Gallery.objects.all().order_by('-id')
    context = {"gallerys" : gallerys}
    return render(request, 'gallery.html', context)

def galleryimage(request, id):
    gallery = models.Gallery.objects.get(id=id)
    galleryimages = models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    context = {"galleryimages" : galleryimages, "gallery": gallery}
    return render(request, 'galleryimages.html', context)


def pricing(request):
    plans = models.Pricing.objects.all().order_by('price')
    dfeatures = models.SubPricing.objects.all()
    context = {"plans" : plans, "dfeatures" : dfeatures}
    return render(request, 'pricing.html', context)

from django.shortcuts import render, redirect
from . import models
from . import forms

from django.shortcuts import render, redirect
from . import forms
from .models import Subscriber

# SignUp
def signup(request):
	msg=None
	if request.method=='POST':
		form=forms.SignUp(request.POST)
		if form.is_valid():
			form.save()
			msg='Thank you for register.'
	form=forms.SignUp
	return render(request, 'registration/signup.html',{'form':form,'msg':msg})

def checkout(request,plan_id):
    planDetails = models.Pricing.objects.get(pk = plan_id)
    context = {"plan" : planDetails}
    return render(request, 'checkout.html', context)


stripe.api_key= 'sk_test_51QCgmiJurtV8dkReO11EI08HV1O8uDEjeFswONigfDS2VSjP4SNOBexd8VvXwKU19cyiAfHtMCwOArwGVhdjl6XK00uzK45iMe'
def checkout_session(request,plan_id):
    plan = models.Pricing.objects.get(pk=plan_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': plan.title,
                    },
                    'unit_amount': plan.price*100,
                },
                'quantity': 1,
            }],
        mode='payment',
    success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
    cancel_url='http://127.0.0.1:8000/cancel',
    client_reference_id=plan_id  # Make sure this is correctly set

    )
    return redirect(session.url, code = 303)

def success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    print('PLAN', plan_id)
    plan = models.Pricing.objects.get(pk=plan_id)
    user = request.user
    models.Subscription.create(
        plan=plan,
        user=user,
        price=plan.price
    )
    # subject='Order Email'
    # html_content = get_template('orderemail.html'.render({'title':plan.title}))
    # msg = EmailMessage(subject, html_content, from_email, [to])
    # msg.content_subtype = "html"
    # msg.send()
    # return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

def user_dashboard(request):
    return render(request, 'user/dashboard.html')

def update_profile(request):
    msg = None
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            msg = "Profile has been updated!"
    form = forms.ProfileForm(instance = request.user)
    context = {'form': form, 'msg' : msg}
    return render(request, 'user/update-profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent logout after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'registration/new_password_form.html', {'form': form})


def trainerlogin(request):
    msg = ' '
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        trainer = models.Trainer.objects.filter(username=username, pwd=pwd).count()
        if trainer > 0:
            request.session['trainerlogin'] = True
            return redirect('trainer_dashboard/')
        else:
            msg = "Invalid!"
    form = forms.TrainerLoginForm()
    context = {"form" : form , 'msg' : msg}
    return render(request, 'trainer/trainerlogin.html', context)

def trainerlogout(request):
    del request.session['trainerlogin']
    return redirect('trainerlogin/')
