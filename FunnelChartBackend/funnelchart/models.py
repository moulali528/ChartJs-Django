from django.db import models

# Create your models here.

class CountryPopulation(models.Model):
    age_group = models.CharField(max_length=10, null=True, blank=True)
    female_population = models.CharField(max_length=10, null=True, blank=True)
    male_population = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.age_group
    
    class Meta:
        verbose_name_plural = 'Country Population'