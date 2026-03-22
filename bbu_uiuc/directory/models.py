from django.utils import timezone
from django.db import models
from django.core.validators import RegexValidator
from django.db.models import UniqueConstraint


class Category(models.Model):
    STATUS_CHOICES = [
        ('0', 'Pending'),
        ('1','Approved')
    ]
    name = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, blank=True)

    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name


class Business(models.Model):
    STATUS_CHOICES = [
        ('0', 'Pending'),
        ('1','Approved')
    ]
    name = models.CharField(max_length=255)
    headline = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    status = models.CharField(choices=STATUS_CHOICES, default='0')
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, blank=True, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message='Please enter valid phone number'
        )
    ])
    address = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='businesses')

    class Meta:
        verbose_name_plural = 'businesses'

    def __str__(self):
        return self.name

    
class Support(models.Model):
    fingerprint = models.CharField(blank=False, max_length=64)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="supports")
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=["fingerprint","business"] ,name="unique_support")
        ]

    def __str__(self):
        return f'{self.business.name} gained a supporter'

        
