"""oasis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

import liam.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',portfolio.views.portfolio, name="home"),
    path('portfolio/',portfolio.views.portfolio, name="portfolio"),
    path('portfolio/1',portfolio.views.one, name="1"),
    path('portfolio/2',portfolio.views.two, name="2"),
    path('portfolio/3',portfolio.views.three, name="3"),
    path('portfolio/4',portfolio.views.four, name="4"),
    path('portfolio/5',portfolio.views.five, name="5"),
    path('portfolio/6',portfolio.views.six, name="6"),
    path('portfolio/6',portfolio.views.seven, name="7"),
    path('portfolio/6',portfolio.views.eight, name="8"),
    path('portfolio/6',portfolio.views.nine, name="9"),
   

]
