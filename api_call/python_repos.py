from matplotlib.pyplot import plot
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

import pygal

myconfig=pygal.Config()
myconfig.x_label_rotation=45
myconfig.show_legend=False
myconfig.title_font_size=24
myconfig.width=1000


url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print (r.status_code)
response_dict=r.json()
# print(response_dict.keys())
# print(response_dict['total_count'])
# print(len(response_dict['items']))

repos=response_dict['items']
repo=repos[0]
names,plot_dicts=[],[]

for repodict in repos:

    
    names.append(repodict['name'])

    
    plot_dict={
        'value':repodict['stargazers_count'],
        'label':repodict['description'],
        'xlink':repodict['html_url']
    }
    plot_dicts.append(plot_dict)
       
mystyle=LS('#333366',base_style=LCS)
chart=pygal.Bar(myconfig,style=mystyle)
chart.title="Most starred projects on github. Click on it to visit the repository :)"
chart.x_labels= names 
chart.y_title="Frequency of visits"
chart.x_title="Names of the projects"   
# chart.add('',stars)
chart.add('',plot_dicts) 
chart.render_to_file('python_repos.svg')

