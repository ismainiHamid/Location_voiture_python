from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.dateparse import parse_date

from locationVoiture.models import Blog, Contact, Vehicule, Client, Reservation

# Create your views here.

contextCars = {}


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
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.subject = request.POST['subject']
        contact.review = request.POST['review']
        contact.save()

        messages.success(request, "This message send with success.")
    return redirect('/contact')


def searchCars(request):
    if request.POST:
        contextCars['datePickUp'] = request.POST["startDate"]
        contextCars['dateReturn'] = request.POST['endDate']
        contextCars['locationPickUp'] = request.POST['startLocation']
        contextCars['locationReturn'] = request.POST['endLocation']
    return render(request, 'search-cars.html', {'vehicule': Vehicule.objects.all()})


def reservation(request, id):
    return render(request, 'reservations.html', {'idVehicule': id})


def reservationSend(request, id):
    vehicule = Vehicule.objects.get(id=id)

    client = Client()
    client.nom = request.POST['firstName']
    client.prenom = request.POST['lastName']
    client.email = request.POST['email']
    client.telephone = request.POST['phone']
    client.cin = request.POST['cine']
    client.permis = request.POST['drive']
    client.save()

    reservation = Reservation()
    reservation.Vehicule = vehicule
    reservation.Client = client
    reservation.depart = 'aéroport'
    reservation.retour = 'Centre Ville'
    reservation.save()

    return redirect('index')
