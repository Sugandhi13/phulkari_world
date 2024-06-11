from django.shortcuts import render
from django.contrib import messages


from .models import Contact
from .forms import ContactForm


# Created contact view that renders info of contact form & update contact model
def contact(request):
    """
    Display an individual :Form:`about.forms.ContactForm`
    and insert record in Contact model.
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
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )