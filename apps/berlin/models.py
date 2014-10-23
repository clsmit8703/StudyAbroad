from django.contrib.gis.db import models

class Student(models.Model):
    """DOC String Here"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    AM_class = models.CharField(max_length=255)
    PM_class = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Professors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school= models.CharField(max_length=255)
    AM_class = models.CharField(max_length=255)
    PM_class = models.CharField(max_length=255)

class Map(models.Model):
    """Represents a point on the map"""
    name = models.CharField(max_length=60)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()
    Latitude = models.DecimalField(max_digits=10, decimal_places=6)
    Longitude = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.Latitude  = self.geom.y
        self.Longitude = self.geom.x
        super(Map, self).save(*args, **kwargs)