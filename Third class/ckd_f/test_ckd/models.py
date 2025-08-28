from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    USER_TYPES = (
        ('doctor', 'Doctor'),
        ('staff', 'Staff'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)  # For doctors
    license_number = models.CharField(max_length=50, blank=True, null=True, unique=True)  # For doctors
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.get_user_type_display()})"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()










class Patient(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('checked', 'Checked'),
    ]
    
    # Personal Information
    phone = models.CharField(
        primary_key=True,
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^01[3-9]\d{8}$',
                message="Phone number must be a valid Bangladeshi mobile number (e.g. 01712345678)"
            )
        ],
        unique=True,
        error_messages={
            'unique': "A patient with this phone number already exists."
        }
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )
    
    # Vital Signs
    upper_bp = models.PositiveIntegerField(verbose_name="Upper BP (mmHg)")
    lower_bp = models.PositiveIntegerField(verbose_name="Lower BP (mmHg)")
    hypertension = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    diabetes = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    coronary_artery_disease = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], blank=True)
    
    # Urine Analysis
    specific_gravity = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(1.03)],
        null=True, blank=True
    )
    albumin = models.PositiveIntegerField(null=True, blank=True)
    sugar = models.PositiveIntegerField(null=True, blank=True)
    red_blood_cells = models.CharField(
        max_length=10, 
        choices=[('normal', 'Normal'), ('abnormal', 'Abnormal')],
        blank=True
    )
    pus_cell = models.CharField(
        max_length=10,
        choices=[('normal', 'Normal'), ('abnormal', 'Abnormal')],
        blank=True
    )
    pus_cell_clumps = models.CharField(
        max_length=10,
        choices=[('present', 'Present'), ('notpresent', 'Not Present')],
        blank=True
    )
    bacteria = models.CharField(
        max_length=10,
        choices=[('present', 'Present'), ('notpresent', 'Not Present')],
        blank=True
    )
    
    # Blood Tests
    blood_glucose = models.FloatField(verbose_name="Blood Glucose (mg/dL)", null=True, blank=True)
    blood_urea = models.FloatField(verbose_name="Blood Urea (mg/dL)", null=True, blank=True)
    serum_creatinine = models.FloatField(verbose_name="Serum Creatinine (mg/dL)", null=True, blank=True)
    sodium = models.FloatField(verbose_name="Sodium (mEq/L)", null=True, blank=True)
    potassium = models.FloatField(verbose_name="Potassium (mEq/L)", null=True, blank=True)
    hemoglobin = models.FloatField(verbose_name="Hemoglobin (g/dL)", null=True, blank=True)
    packed_cell_volume = models.FloatField(null=True, blank=True)
    white_blood_cell = models.FloatField(verbose_name="WBC (cells/cmm)", null=True, blank=True)
    red_blood_cell = models.FloatField(verbose_name="RBC (millions/cmm)", null=True, blank=True)
    
    # Clinical Findings
    pedal_edema = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    anemia = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    appetite = models.CharField(max_length=10, choices=[('good', 'Good'), ('poor', 'Poor')])
    
    # System
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ['-created_at']