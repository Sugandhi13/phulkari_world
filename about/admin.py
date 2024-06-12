# Importing required libraries to register the models

from django.contrib import admin
from .models import About, Contact


# Register About model
class AboutAdmin(admin.ModelAdmin):

    list_display = (
                    'title', 
                    'content', 
                    'updated_on'
                    )


admin.site.register(About, AboutAdmin)



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


admin.site.register(Contact, ContactAdmin)