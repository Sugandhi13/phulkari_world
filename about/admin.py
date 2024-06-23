# Importing required libraries to register the models

from django.contrib import admin
from .models import About, Contact, Faq


# Register About model
class AboutAdmin(admin.ModelAdmin):

    list_display = (
                    'title',
                    'content',
                    'updated_on'
                    )


# Register Contact model
class ContactAdmin(admin.ModelAdmin):

    list_display = (
                    'name',
                    'email',
                    'message',
                    'read',
                    'created_on'
                )

    ordering = ('created_on',)


# Register Faq model
class FaqAdmin(admin.ModelAdmin):

    list_display = (
                    'query',
                    'answer',
                    'updated_on'
                    )


admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Faq, FaqAdmin)
