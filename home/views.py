# Import required libraries to configure views

from django.shortcuts import render


# Created index views
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
