import json
import math
from country_codes import get_country_code
from pygal.maps.world import COUNTRIES
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename='population_data.json'
with open(filename, 'r') as f:
    pop_data=json.load(f)
    
    
    cc_population={}
    for pop_dict in pop_data:
        if pop_dict['Year']=='2010':
            
            country_name=pop_dict['Country Name']
            population=int(float((pop_dict['Value'])))
            code=get_country_code(country_name)
            if code:
                cc_population[code]=population
                
                
                
    ccp1,ccp2,ccp3={},{},{}
    for c,p in cc_population.items():
        if p<10000000 :
            ccp1[c]=p 
        elif p<100000000:
            ccp2[c]=p
        else:
            ccp3[c]=p  
            
              
    print(len(ccp1),len(ccp2),len(ccp3))  
    
    wm_style=RotateStyle('#336699', base_style=LightColorizedStyle)
    wm=pygal.maps.world.World(style=wm_style)
    
    wm.title="world map pop in 2010"
    wm.add('0-10m',ccp1)
    wm.add('10m-1b',ccp2)
    wm.add('>1b',ccp3)
    wm.render_to_file('world_pop.svg')
    
    