from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('services',views.services,name='services'),
     path('contact_form',views.contact_form,name='contact_form'),
   
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/',views.admin,name='admin'),
    path('adminlogout/',views.logoutadmin,name='adminlogout'),

    # path('services/', views.service_details, name='service_details'),
    # path('admin/services/add/', views.add_service, name='add_service'),
    # path('admin/services/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    # path('admin/services/<int:service_id>/', views.view_service, name='view_service'),
    # path('admin/services/<int:service_id>/delete/', views.delete_service, name='delete_service'),

    path('contactmessages/', views.contact_details, name='contact_details'),
    path('admin/contactmessages/<int:contact_id>/', views.view_contact, name='view_contact'),
    path('admin/contactmessages/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),

]
