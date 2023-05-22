from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_date

from locationVoiture.models import Blog, Contact, Vehicule, Client, Reservation


# Create your views here.

def index(request):
    blog_dict = Blog.objects.all().order_by('-date')[:3]
    context = {
        'blog': blog_dict,
    }
    return render(request, 'index.html', context)


def blog(request):
    blog_dict = Blog.objects.all().order_by('-date')
    context = {
        'blog': blog_dict,
    }
    return render(request, 'blog.html', context)


def blogDetails(request, id):
    blog_dict = Blog.objects.all().order_by('-date')[:5]
    blog_details = Blog.objects.filter(id=id).first()
    context = {
        'blog_side': blog_dict,
        'blog_details': blog_details,
    }
    return render(request, 'blog-details.html', context)


def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        review = request.POST['review']

        contact = Contact()
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.review = review

        contact.save()

        messages.success(request, "This message send with success.")
    return redirect('/contact')


def searchCars(request):
    global context
    if request.POST:
        context = {
            'datePickUp': request.POST['startDate'],
            'dateReturn': request.POST['endDate'],
            'locationPickUp': request.POST['startLocation'],
            'locationReturn': request.POST['endLocation'],
            'vehicule': Vehicule.objects.all()
        }
    return render(request, 'search-cars.html', context)


def reservation(request):
    global context
    if request.POST:
        context = {
            'datePickUp': request.POST['startDate'],
            'dateReturn': request.POST['endDate'],
            'locationPickUp': request.POST['startLocation'],
            'locationReturn': request.POST['endLocation'],
            'vehicule': Vehicule.objects.filter(id=id).first()
        }
    return render(request, 'reservations.html', context)


def reservationSend(request, id):
    client = Client()
    client.nom = request.POST['firstName'],
    client.prenom = request.POST['lastName'],
    client.email = request.POST['email'],
    client.telephone = request.POST['phone'],
    client.cin = request.POST['cine'],
    client.permis = request.POST['drive'],
    c = client.save()

    reservation = Reservation()
    reservation.Vehicule = Vehicule.objects.filter(id=id).first()
    reservation.Client = c,
    reservation.dateDebut = request.POST['startDate'],
    reservation.dateFin = request.POST['endDate'],
    reservation.depart = request.POST['startLocation'],
    reservation.retour = request.POST['endLocation'],
    reservation.save()

    return redirect('index')