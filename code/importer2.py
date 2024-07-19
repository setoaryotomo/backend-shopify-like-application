import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, *[os.pardir] * 3)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopify.settings'
import django
django.setup()

import json
from metafield.models import Metafield

filepath = './dummy-data/'


# Import Metafields
with open(filepath + 'metafield.json') as jsonfile:
    metafields = json.load(jsonfile)
    for meta in metafields:
        Metafield.objects.create(
            description=meta['description'],
            key=meta['key'],
            namespace=meta['namespace'],
            owner_id=meta['owner_id'],
            owner_resource=meta['owner_resource'],
            value=meta['value'],
            type=meta['type']
        )