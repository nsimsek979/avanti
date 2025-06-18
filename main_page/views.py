from django.shortcuts import render
from .models import (Index, OurApproach, ChooseUs,  
                     Clients, SourcingSolutions, 
                     ConsultancyServices, Visitor, OurStory,
                     Service, ProductCategory, Products, Adress)
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.utils import timezone
from datetime import timedelta
from django.db import models





# Create your views here.
def index(request):
    queryset = Index.objects.all().order_by('-updated_at')[:3]
    approach_qs = OurApproach.objects.all()
    chooseus_qs = ChooseUs.objects.all()
    our_story = OurStory.objects.last()
    context = {
        "queryset": queryset,
        "ourapp": approach_qs,
        "chooseus": chooseus_qs,
        "our_story": our_story,
    }
    return render(request, "index.html", context)







def contact(request):
    adress = Adress.objects.first()
   


    if request.method == 'POST':
       
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            # Save to database
            message = form.save()
            
            # Send email
            send_mail(
                subject=f"New Contact Form Submission: {message.subject}",
                message=f"""
                Name: {message.name}
                Email: {message.email}
                Subject: {message.subject}
                Message: {message.message}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],  # Your email here
                fail_silently=False,
            )

            return render(request, 'contact.html', {
                'form': ContactForm(),
                'success': True     })
    else:
        form = ContactForm()

    context={
        'form': form,
        "adress" : adress
    }
    
    return render(request, 'contact.html', context)

def about(request):
    clients= Clients.objects.all()
    approach_qs = OurApproach.objects.all()
    chooseus_qs = ChooseUs.objects.all()
    context = {
        "clients" : clients,       
        "ourapp": approach_qs,
        "chooseus": chooseus_qs,
    }
    return render(request, "about.html", context)




def products(request):
    category = ProductCategory.objects.all()
    products = Products.objects.all()

    context = {
        "categories": category,
        "products" :products,
    }
    return render(request, "portfolio.html", context)



def services(request):
    sorc_solutions= SourcingSolutions.objects.all()
    cons_services = ConsultancyServices.objects.all()
    service_description = Service.objects.last()
    
  
    context = {
        "sour_solutions" : sorc_solutions, 
        "cons_services" : cons_services,
        "service": service_description,    
    }
    return render(request, "services.html", context)


def analytics_dashboard(request):
    # Get all time stats
    all_visitors = Visitor.objects.all()
    all_count = all_visitors.count()
    
    # Get this week's stats
    week_ago = timezone.now() - timedelta(days=7)
    week_visitors = Visitor.objects.filter(timestamp__gte=week_ago)
    week_count = week_visitors.count()
    
    # Get this month's stats
    month_ago = timezone.now() - timedelta(days=30)
    month_visitors = Visitor.objects.filter(timestamp__gte=month_ago)
    month_count = month_visitors.count()
    
    # Get this year's stats
    year_ago = timezone.now() - timedelta(days=365)
    year_visitors = Visitor.objects.filter(timestamp__gte=year_ago)
    year_count = year_visitors.count()
    
    # Get top countries
    top_countries = Visitor.objects.exclude(country__isnull=True)\
                         .values('country')\
                         .annotate(count= models.Count('country'))\
                         .order_by('-count')[:10]
    
    context = {
        'all_count': all_count,
        'week_count': week_count,
        'month_count': month_count,
        'year_count': year_count,
        'top_countries': top_countries,
    }
    
    return render(request, 'analytics/dashboard.html', context)





