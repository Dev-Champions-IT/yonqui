from django.db import models


class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
    

class SocialLink(models.Model):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform


# Yonqui Membership Application Model
from django.core.validators import RegexValidator

class MemberApplication(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?\d{9,15}$')])
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Nigeria')
    tribe = models.CharField(max_length=100, default='Yoruba')
    is_yoruba = models.BooleanField(default=True)
    passport_id_number = models.CharField(max_length=50)
    passport_id_type = models.CharField(max_length=50, choices=[('passport', 'Passport'), ('national_id', 'National ID'), ('voters_card', 'Voters Card'), ('other', 'Other')])
    passport_id_image = models.ImageField(upload_to='uploads/passports/')
    occupation = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    reason_for_joining = models.TextField(blank=True)
    date_applied = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name