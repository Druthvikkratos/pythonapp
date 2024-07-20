"""
URL configuration for Appzia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ecoplast_app.views import admin
from ecoplast_app import views 

# from django.contrib.sitemaps.views import sitemap
# from ecoplast_app.sitemaps import MySitemap
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin', admin,name='admin'),
    path('',include('ecoplast_app.urls')),
   
   
  
    path('admin/',views.admin, name='admin'),  

    # path('sitemap.xml', sitemap, {'sitemaps': {'my_sitemap': MySitemap}}, name='django.contrib.sitemaps.views.sitemap'),
    # path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")), 

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)