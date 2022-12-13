from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class FlairUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

    # overwrite delete method
    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class HealthForm(models.Model):
    TRAVELED_WITHIN_LAST_TWO_WEEKS = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    EXPERIENCING_SYMPTOMS = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    traveled_within_last_two_weeks = models.CharField(null=True, blank=True, max_length=255, choices=TRAVELED_WITHIN_LAST_TWO_WEEKS)
    travel_location = models.CharField(null=True, blank=True, max_length=255)
    experiencing_symptoms = models.CharField(null=True, blank=True, max_length=255, choices=EXPERIENCING_SYMPTOMS)
    specify_symptoms = models.CharField(null=True, blank=True, max_length=255)
    vaccine_card = models.ImageField(upload_to='uploads/vaccine_cards')
    user_photo = models.ImageField(upload_to='uploads/student_images')
    health_form_submitted_by = models.ForeignKey(FlairUser, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)