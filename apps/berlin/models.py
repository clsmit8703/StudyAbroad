from django.contrib.gis.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')


class Student(models.Model):
    """Represents the student's information in the database"""
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
    school = models.CharField(max_length=255)
    AM_class = models.CharField(max_length=255)
    PM_class = models.CharField(max_length=255)


class Popular_Places(models.Model):
    """Represents a point on the map"""
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()
    Latitude = models.DecimalField(max_digits=10, decimal_places=6)
    Longitude = models.DecimalField(max_digits=10, decimal_places=6)


    def __str__(self):
        return "{}".format(self.name)

    def save(self, *args, **kwargs):
        self.geom.y = self.Latitude
        self.geom.x = self.Longitude
        super(Popular_Places, self).save(*args, **kwargs)

class Images(models.Model):
    """Pics model."""
    name = models.CharField(max_length=100)
    place = models.ForeignKey(Popular_Places)
    photo = models.ImageField(storage =fs)

    def __str__(self):
        return self.name



class Georgia(models.Model):
    """Represents the state of Georgia on a map"""
    name = models.CharField(max_length=100)
    num_studen = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return "{}".format(self.name)
