from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import enquiry

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
        return HttpResponseRedirect('/contact-us/')
        #return render(request, 'contact-us.html', {"message": "Congrats, Data Submitted Successfully."})
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


