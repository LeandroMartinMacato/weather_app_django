from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length = 40 )
    address = models.CharField(max_length = 200 , null = True  , blank = True )
    lat = models.CharField(max_length = 40 , null = True , blank = True)
    long = models.CharField(max_length = 40 , null = True , blank = True)

    # coordinates = 

    def __str__(self):
        return self.name