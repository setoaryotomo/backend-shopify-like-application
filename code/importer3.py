import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, *[os.pardir] * 3)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopify.settings'
import django
django.setup()

import json
# from discount.models import PriceRule, DiscountCode
from discount.models import DiscountCode

filepath = './dummy-data/'

# # Import PriceRule data  
# with open(filepath+'pricerule.json') as jsonfile:  
#     pricerules = json.load(jsonfile)  
# for pricerule in pricerules:  
#     PriceRule.objects.create(  
#         id=pricerule['id'],  
#         title=pricerule['title'],  
#         target_type=pricerule['target_type'].strip(),  
#         target_selection=pricerule['target_selection'].strip(),  
#         allocation_method=pricerule['allocation_method'],  
#         value_type=pricerule['value_type'],  
#         # value_type_list=pricerule['value'],  
#         value=pricerule['value'],  
#         starts_at=pricerule['starts_at'],  
#         ends_at=pricerule['ends_at'],  
#         created_at=pricerule['created_at'],  
#         updated_at=pricerule['updated_at']  
#     )  
 
  
# Import Discount data  
with open(filepath+'discountcode.json') as jsonfile:  
    discountcodes = json.load(jsonfile)  
for discountcode in discountcodes:  
    DiscountCode.objects.create(  
        code=discountcode['code'],  
        created_at=discountcode['created_at'],  
        updated_at=discountcode['updated_at'],  
        id=discountcode['id'],  
        price_rule_id=discountcode['price_rule'],  
        usage_count=discountcode['usage_count'],  
        errors=discountcode['errors']  
    )  