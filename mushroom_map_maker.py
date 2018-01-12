'''
~~~~~~~~~~
Mushroom map maker

This program asks a user for the genus and species of
a mushroom and uses that information to render a heatmanp
of that mushroom's distribution across the globe.
'''
from gmplot import gmplot
import requests

def generate_url(genus_name, species_name):
    full_name = '{}+{}'.format(genus_name, species_name)
    url = 'http://mushroomobserver.org/api/observations?name={}&detail=low&format=json'.format(full_name)
    return url


def get_raw_results(url):
    ''' Function requests response from
    mushroomobserver.com in the form of JSON data, which
     includes GPS data from observations of the user defined mushroom.'''
    mushroom_request = requests.get(url)
    raw_results = mushroom_request.json()
    return raw_results

def get_location_data(raw_results):
    '''Function parses JSON data from get_raw_results() to isolate GPS data
    for observations of the user defined mushroom.'''
    print('getting location data..')
    latitude_list = []
    longitude_list = []
    for item in raw_results['results']:
        latitude_north_limit = item['location']['latitude_north']
        latitude_south_limit = item['location']['latitude_south']
        longitude_east_limit = item['location']['longitude_east']
        longitude_west_limit = item['location']['longitude_west']
        latitude = (latitude_north_limit + latitude_south_limit) / 2
        longitude = (longitude_east_limit + longitude_west_limit) / 2
        latitude_list.append(latitude)
        longitude_list.append(longitude)
    return latitude_list, longitude_list

def draw_map(latitude_list, longitude_list):
    '''Function uses the gmplot package to render an html pagge to the user
    with the distribution of the user defined mushroom.'''
    print('drawing map...')
    gmap = gmplot.GoogleMapPlotter(40.078729, -97.131828, 4)
    #gmap.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=10)
    #gmap.scatter(latitude_list, longitude_list, '#3B0B39', size=40, marker=False)
    #gmap.scatter(latitude_list, longitude_list, 'k', marker=True)
    gmap.heatmap(latitude_list, longitude_list, threshold=10, radius=30, gradient=None, opacity=0.6, dissipating=True)
    gmap.draw("mushroom_map.html")
    print('map is complete!')

def run(genus_name, species_name):
    url = generate_url(genus_name, species_name)
    raw_results = get_raw_results(url)
    latitude_list, longitude_list = get_location_data(raw_results)
    draw_map(latitude_list, longitude_list)












