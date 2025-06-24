from django.contrib import admin
from .models import (Index, OurApproach, 
                     ChooseUs, ContactMessage, Clients, 
                     SourcingSolutions, ConsultancyServices,
                    Visitor, OurStory,ProductCategory, Products,
                    Service, Adress)

# Register your models here.
admin.site.register(Index)
admin.site.register(OurApproach)
admin.site.register(ChooseUs)
admin.site.register(ContactMessage)
admin.site.register(Clients)
admin.site.register(SourcingSolutions)
admin.site.register(ConsultancyServices)
admin.site.register(Visitor)
admin.site.register(OurStory)
admin.site.register(Service)
admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(Adress)


