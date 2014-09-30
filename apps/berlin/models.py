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
