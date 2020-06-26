from django.shortcuts import render, redirect
from .models import enquiry
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about-us.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['con_name']
        email = request.POST['con_email']
        phone = request.POST['con_contact']
        subject = request.POST['con_subject']
        description = request.POST['con_message']
        status = False

        result = enquiry.objects.create(name=name, email=email, contact=phone, subject=subject, description=description,
                                        status=status)
        result.save()
        messages.success(request, "Your message successfully sent!")
        return redirect('contact-us')
    else:
        return render(request, 'contact-us.html')


def history(request):
    return render(request, 'our-history.html')


def leadership(request):
    return render(request, 'leadership.html')


def why_choose_us(request):
    return render(request, 'why-choose-us.html')


def career(request):
    return render(request, 'career.html')


def projects(request):
    return render(request, 'projects.html')

