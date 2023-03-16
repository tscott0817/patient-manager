from django.db import models

# Create your models here.
class PatientDemo(models.Model):
    # id = models.AutoField(primary_key=True)  # TODO: Not sure if key is auto generated
    name_last = models.CharField(max_length=100)
    name_first = models.CharField(max_length=100)
    dob = models.DateField()
    sex = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)  # TODO: Need to created images directory

# class PatientContact(models.Model):
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#
#     # TODO: Maybe separate out employer info
#     employer = models.CharField(max_length=100)
#     employer_phone = models.CharField(max_length=100)

# class PatientEmergency(models.Model):
#     name = models.CharField(max_length=100)
#     relationship = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)



    def __str__(self):
        return self.name_last