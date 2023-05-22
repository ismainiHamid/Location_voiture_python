from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.searchCars, name='search'),
    path('reservation/<int:id>', views.reservation, name='reservation'),
    path('reservation/send/<int:id>', views.reservationSend, name='reservationSend'),

    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('service', TemplateView.as_view(template_name='service.html'), name='service'),

    path('blog', views.blog, name='blog'),
    path('blog/<int:id>', views.blogDetails, name='blog'),

    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('contact/send', views.contact, name='contactSend')
]
