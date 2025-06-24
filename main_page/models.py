from django.db import models
from django.utils import timezone


class Index(models.Model):
    carousel_header = models.CharField(max_length=150, verbose_name="Carousel Tanım")
    carousel_line = models.CharField(max_length=300, verbose_name="Carousel Açıklama")
    image = models.ImageField( upload_to="carousal-image")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return  f"{self.carousel_header}"
    
class OurStory(models.Model):
    name =models.CharField(default="Our Story", max_length=50)
    description = models.TextField(max_length=1000, verbose_name="Açıklama")
    image = models.ImageField( upload_to="OurStory")

    def __str__(self):
        return  f"{self.name}"

    

class OurApproach(models.Model):
    approach_header = models.CharField(max_length=150, verbose_name="Yaklaşımımız")
    approach_line = models.TextField(max_length=1000, verbose_name="Yaklaşımımız Açıklama")   
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return  f"{self.approach_header}"
    
class ChooseUs(models.Model):
    chooseus_header = models.CharField(max_length=150, verbose_name="Neden Biz")
    chooseus_line = models.CharField(max_length=300, verbose_name="Neden Biz Açıklama")
    image = models.ImageField( upload_to="carousal-image")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return  f"{self.chooseus_header}"
    
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
    name = models.CharField(max_length=100, verbose_name="Müşteri Adı")
    image = models.ImageField( upload_to="client-image", verbose_name="Müşteri Logo")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name
    
class SourcingSolutions(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kaynak Çözümler")
    description = models.TextField(max_length=500, verbose_name="Açıklama")
    image = models.ImageField( upload_to="sourcing-solution", null=True, blank=True)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.name
    

class ConsultancyServices(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Danışmanlık Hizmeti")
    description = models.TextField(max_length=1000, verbose_name="Açıklama")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.name
    
class Service(models.Model):
    service_description = models.TextField()
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
     
    def __str__(self):
        return f"{self.updated_at}"
    

class ProductCategory(models.Model):
    name = name = models.CharField(max_length=100, verbose_name="Kategori")
    image = models.ImageField( upload_to="category", null=True, blank=True)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = name = models.CharField(max_length=100, verbose_name="Ürünler")
    category = models.ForeignKey(ProductCategory,  on_delete=models.CASCADE, related_name="category")
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name

class Adress(models.Model):
    location = models.CharField( max_length=350)
    email = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    google_map =models.CharField( max_length=850)
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)


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