from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length = 20 )
    # coordinates = 

    def __str__(self):
        return self.name