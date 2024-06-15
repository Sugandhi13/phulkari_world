""" Veiws for newsletter app """
from django.shortcuts import render


def newsletter(request):
    """ Return newsletter signup page view.
    """
    site_area = request.path

    context = {
        'site_area': site_area,
    }

    return render(request, 'newsletter/newsletter-subscribe.html', context)