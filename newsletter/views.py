from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from products.models import ProductFeatured, Product
from .forms import ContactForm, SignUpForm
from .models import SignUp


def home(request):

    featured_image = ProductFeatured.objects.first()
    products = Product.objects.all().order_by("?")[:4]

    # form = SignUpForm(request.POST or None)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     email = form.cleaned_data.get('email')
    #     user_id, domain = email.split('@')
    #     full_name = form.cleaned_data.get('full_name')
    #     if not full_name:
    #         full_name = user_id
    #     instance.full_name = full_name
    #     instance.save()
    #     return redirect('sign_up_successful.html')
    context = {
        # 'form': form,
        'featured_image': featured_image,
        'products': products,
    }
    # if request.user.is_authenticated() and request.user.is_staff:
    #     data = SignUp.objects.all()
    #     context = {
    #         'data': data
    #     }
    return render(request, 'home.html', context)


def sign_up_successful(request):
    return render(request, 'sign_up_successful.html', {})


def message_submitted(request):
    return render(request, 'contact_us_submitted.html', {})


def contact(request):

    form = ContactForm(request.POST or None)
    # we would use the below if we wanted to send an email.
    """
    if form.is_valid():

        # get values typed into form
        form_email = form.cleaned_data.get('email')
        form_name = form.cleaned_data.get('name')
        form_message = form.cleaned_data.get('message')

        # construct email from typed info
        subject = 'Site contact form'
        message = "{} via {}would like to know: \n{}".format(
            form_name,
            form_email,
            form_message
        )
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'anotheremail@somedomain.com']

        # send the email
        send_mail(subject,
                  message,
                  from_email,
                  to_email,
                  fail_silently=True)
        """
    return render(request, 'contact.html', {'form': form})
