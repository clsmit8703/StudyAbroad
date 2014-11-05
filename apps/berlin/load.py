import os
from django.contrib.gis.utils import LayerMapping
from models import Georgia
import django
django.setup()

ga_mapping = {
    'name': 'name',
    'num_studen': 'num_studen',
    'lon': 'long_x_',
    'lat': 'lat_Y_',
    'mpoly': 'POINT',
}

ga_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/colleges.shp'))


def run(verbose=True):
    lm = LayerMapping(Georgia, ga_shp, ga_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)