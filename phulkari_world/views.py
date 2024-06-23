# Import required libraries to configure views

from django.shortcuts import render


# Configure error 404 view
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
