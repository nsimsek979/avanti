from django.contrib import admin
from .models import Index, OurApproach, ChooseUs, ContactMessage, Clients, SourcingSolutions, ConsultancyServices, Visitor

# Register your models here.
admin.site.register(Index)
admin.site.register(OurApproach)
admin.site.register(ChooseUs)
admin.site.register(ContactMessage)
admin.site.register(Clients)
admin.site.register(SourcingSolutions)
admin.site.register(ConsultancyServices)
admin.site.register(Visitor)