import json
import math

from matplotlib.pyplot import get
from pygal.maps.world import COUNTRIES



# with open('population_data.json') as f:
#     l=json.load(f)
#     for pop_dict in l:
#         if pop_dict['Year']==2010:
#             name=pop_dict['Country Name']
#             code=
        
        
        
        

def get_country_code(country_name):
    l=sorted(COUNTRIES.items())
    for (code,country) in l:
        if country==country_name:
            return code
    return "doesnt exist"    
        

            
