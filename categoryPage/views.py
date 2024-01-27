from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def categoryPage_index_view(request) :
    '''This function render index page of ecommerce view'''

    return HttpResponse(" Welcome to 6410742131 Tawan Phonsapsin categoryPage views!")
