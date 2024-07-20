from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def contact_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save the form data, including the uploaded file, to the database
            return render(request, 'contact.html', {'form': MyForm(), 'success_message': "Thank you for contacting Ecoplast Interiors"})
    else:
        form = MyForm()

    return render(request, 'contact.html', {'form': form})


from django.views.decorators.cache import never_cache   
from django.contrib.auth import authenticate 
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404

@never_cache
def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin/dashboard.html')
    return redirect('admin')

def admin(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    if request.method == "POST":
        form = adminform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')  # Ensure this URL name is correct
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
                return redirect('admin')  # Ensure this URL name is correct

    else:
        form = adminform()

    return render(request, 'admin/adminlogin.html', {'form': form})




@never_cache
def logoutadmin(request):
    if request.user.is_authenticated:
        logout(request)
    # Redirect to a page that ensures users cannot navigate back
    return redirect('admin')



# contact messages
@never_cache
def contact_details(request):
    if request.user.is_authenticated:
        contact = Contact_Messages.objects.all()
        return render(request, 'admin/contactmessages/contactmessage.html', {'contact': contact})
    return redirect('admin')

def delete_contact(request, contact_id):
    if request.user.is_authenticated:
        contact = get_object_or_404(Contact_Messages, pk=contact_id)
        if request.method == 'POST':
            contact.delete()
            # messages.success(request, 'Gallery deleted successfully.')
            return redirect('contact_details')
        return render(request, 'admin/contactmessages/contactdelete.html', {'contact': contact})
    return redirect('admin')

@never_cache
def view_contact(request, contact_id):
     if request.user.is_authenticated:
         contact = get_object_or_404(Contact_Messages, pk=contact_id)
         return render(request, 'admin/contactmessages/contactview.html', {'contact': contact})
     return redirect('admin')




# Services

@never_cache
def service_details(request):
    if request.user.is_authenticated:
        service = services.objects.all()
        return render(request, 'admin/services/services.html', {'service': service})
    return redirect('admin')


@never_cache

def add_service(request):
   if request.user.is_authenticated:
        service = services.objects.all()  # Move this line outside of the if condition
        if request.method == 'POST':
            form = serviceForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('service_details')
        else:
            form = serviceForm()
        return render(request, 'admin/services/addservice.html', {'form': form, 'service': service})

   return redirect('admin/services')

@never_cache
def edit_service(request, service_id):
    if request.user.is_authenticated:
        service = get_object_or_404(services, pk=service_id)
        form = serviceForm(request.POST or None, request.FILES or None, instance=service)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('service_details')
        return render(request, 'admin/services/editservice.html', {'form': form, 'service': service})
    return redirect('admin')

@never_cache
def delete_service(request, service_id):
    if request.user.is_authenticated:
        service = get_object_or_404(services, pk=service_id)
        if request.method == 'POST':
            service.delete()
            # messages.success(request, 'Gallery deleted successfully.')
            return redirect('service_details')
        return render(request, 'admin/services/deleteservice.html', {'service':service})
    return redirect('admin')

@never_cache

def view_service(request, service_id):
     if request.user.is_authenticated:

         service = get_object_or_404(services, pk=service_id)
         return render(request, 'admin/services/viewservice.html', {'service': service})
     return redirect('admin')

