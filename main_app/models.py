from django.db import models

# Create your models here.
GENDERS_CHOICE = (
    ('F', 'Female'),
    ('M', 'Male')
)

class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_lastname = models.CharField(max_length=50)
    patient_species = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(
        max_length=1,
        choices=GENDERS_CHOICE
    )
    patient_weight = models.IntegerField()
    color_color = models.CharField(max_length=50)

    def __str__(self):
        return self.patient_name