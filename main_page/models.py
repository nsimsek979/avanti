from django.db import models
from django.utils import timezone


class Index(models.Model):
    carousel_header = models.CharField(max_length=150)
    carousel_line = models.CharField(max_length=300)
    image = models.ImageField( upload_to="carousal-image")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return  f"{self.created_at}"

class OurApproach(models.Model):
    approach_header = models.CharField(max_length=150)
    approach_line = models.CharField(max_length=500)   
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return  f"{self.created_at}"
    
class ChooseUs(models.Model):
    chooseus_header = models.CharField(max_length=150)
    chooseus_line = models.CharField(max_length=300)
    image = models.ImageField( upload_to="carousal-image")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return  f"{self.created_at}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

class Clients (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to="client-image")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name
    
class SourcingSolutions(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.name
    

class ConsultancyServices(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.name

# models.py

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(null=True, blank=True)
    referrer = models.URLField(null=True, blank=True)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        ordering = ['-timestamp']