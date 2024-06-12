from django.shortcuts import render
from django.contrib import messages


from .models import About, Contact
from .forms import ContactForm


# Created about_me view that renders all info of about model
def about_us(request):
    """
    Display and insert record in About model.
    """
    aboutset = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about_us.html",
        {
            "about": aboutset
        },
    )


# Created contact view that renders info of contact form & update contact model
def contact(request):
    """
    Display a ContactForm and insert record in Contact model.
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for contacting us. We will respond within 2 days.'
            )
        else:
            messages.error(
                request,
                'Message failed. Please ensure data filled in all fields are valid.'
            )

    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {
            "contact_form": contact_form
        },
    )

def faq(request):
    """ A view to return contact success page """

    return render(request, 'about/faq.html')