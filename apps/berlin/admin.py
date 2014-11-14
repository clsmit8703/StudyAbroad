from django.contrib.gis import admin
from apps.berlin import models


class MapAdmin(admin.OSMGeoAdmin):
    readonly_fields = ('Latitude', 'Longitude')


# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Popular_Places, admin.OSMGeoAdmin)
admin.site.register(models.Georgia, admin.OSMGeoAdmin)
admin.site.register(models.Images)

