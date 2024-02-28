from django.db import models
  

class VaccinationCenter(models.Model):
  name = models.CharField(max_length=150)
  address = models.CharField(max_length=200)
  working_hours = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  

class VaccinationSlot(models.Model):
  center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)
  date = models.DateField(auto_now=False)
  name = models.CharField(max_length=150, null=False, blank=False, default='')
  phone_number = models.CharField(max_length=20, null=False, blank=False, default='')

  def __str__(self):
    return self.name
  

class DosageDetail(models.Model):
  center_name = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE, default=None)
  vaccine_name = models.CharField(max_length=150)

  def __str__(self):
      return self.vaccine_name
  

