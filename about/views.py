from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import About, Contact, Faq
from .forms import AboutForm, ContactForm, FaqForm


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


@login_required
def edit_about_us(request):
    """ Edit About us page of the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    about_us = get_object_or_404(About)
    if request.method == 'POST':
        about_form = AboutForm(request.POST, request.FILES, instance=about_us)
        if about_form.is_valid():
            about_form.save()
            messages.success(request, 'Successfully updated About Us!')
            return redirect(reverse('about'))
        else:
            messages.error(
                request,
                'Failed to update about us. Please ensure the form is valid.'
            )
    else:
        about_form = AboutForm(instance=about_us)
        messages.info(request, f'You are editing About Us')

    template = 'about/edit_about_us.html'
    context = {
        'about_form': about_form,
        'about_us': about_us,
    }

    return render(request, template, context)


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
                'Message failed. Please ensure data in all fields are valid.'
            )

    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {
            "contact_form": contact_form
        },
    )


# Created faq view that renders all info of Faq model
def faq(request):
    """
    Display and insert record in About model.
    """
    aboutset = Faq.objects.all()

    return render(
        request,
        "about/faq.html",
        {
            "faqs": aboutset
        },
    )


@login_required
def add_faq(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        faq_form = FaqForm(request.POST)
        if faq_form.is_valid():
            faq = faq_form.save()
            messages.success(
                request, f'Successfully added query "{faq.query}"')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request,
                f'Failed to add {faq.query}. Please ensure the form is valid.'
            )
    else:
        faq_form = FaqForm()

    template = 'about/add_faq.html'
    context = {
        'faq_form': faq_form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """ Edit Faq page of the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        faq_form = FaqForm(request.POST, request.FILES, instance=faq)
        if faq_form.is_valid():
            faq_form.save()
            messages.success(
                request, f'Successfully updated query "{faq.query}"')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request,
                f'Failed to update "{faq.query}". Make sure the form is valid.'
            )
    else:
        faq_form = FaqForm(instance=faq)
        messages.info(request, f'You are editing query "{faq.query}"')

    template = 'about/edit_faq.html'
    context = {
        'faq_form': faq_form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, f'Query "{faq.query}" deleted!')
    return redirect(reverse('faq'))
