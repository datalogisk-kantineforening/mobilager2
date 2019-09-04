"""mobilager2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from inventory import views

urlpatterns = [
    url(r'^$', views.stock, name='stock'),
    url(r'^stock/?$', views.stock, name='Lagerbeholdning'),
    url(r'^restock/?$', views.restock, name='Levering'),
    url(r'^replenish/?$', views.replenish, name='Opfyldning'),
    url(r'^correction/?$', views.correction, name="Korrektion"),
    url(r'^history/?$', views.history, name='Historik'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/?$',
        auth_views.LoginView.as_view(template_name='login.html'),
        name="django.contrib.auth.views.login"),
    url(r'^accounts/logout/?$',
        auth_views.LogoutView.as_view(next_page='/'),
        name="django.contrib.auth.views.logout"),
    url(r'^fragments/addform/?$', views.addform_fragment, name="addform_fragment"),
    url(r'^fragments/addbtn/?$', views.addbtn_fragment, name="addbtn_fragment"),
]
