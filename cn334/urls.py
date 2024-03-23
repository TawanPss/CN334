"""
URL configuration for cn334 project.

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
from django.urls import path

from ecommerce import views as ecom_views
from homePage import views as homePage_views
from categoryPage import views as categoryPage_views
from productPage import views as productPage_views
from checkOutPage import views as checkOutPage_views
from contactPage import views as contactPage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/', ecom_views.ecommerce_index_view),
    path('ecommerce/item/<item_id>', ecom_views.item_view),
    path('homePage/', homePage_views.homePage_index_view),
    path('category/',categoryPage_views.categoryPage_index_view),
    path('product',productPage_views.productPage_index_view),
    path('checkOut',checkOutPage_views.checkOutPage_index_view),
    path('contact',contactPage_views.contactPage_index_view),
    path("W09/request", ecom_views.basic_request),
    path("W09/tokenize", ecom_views.tokenize),
    path("W09/sentimental", ecom_views.sentimental),
    path("W09/text2speech", ecom_views.text2speech)
]
