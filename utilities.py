import tldextract
import socket
import requests
import matplotlib.pyplot as plt
import geopandas 


API_URL = "http://ip-api.com/json/" 


def user_info():

    IP = requests.get('https://api64.ipify.org?format=json').json()['ip']

    if (info := requests.get(API_URL + IP).json())['status'] == "success":
        return info

    return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}

def information(string):

    try:

        socket.inet_aton(string) # string is the IP

        if (info := requests.get(API_URL + string).json())['status'] == "success":
            return info
        
        return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}

    except:

        try:

            extracted = tldextract.extract(string)
            if extracted.subdomain:
                IP = socket.gethostbyname(f'{extracted.subdomain}.{extracted.domain}.{extracted.suffix}')
            else:
                IP = socket.gethostbyname(f'www.{extracted.domain}.{extracted.suffix}')

            if (info := requests.get(API_URL + IP).json() )['status'] == "success":
                return info
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}

        except:
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}
        


def plot_map(info):

    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

    fig, ax = plt.subplots(figsize=(8,6))
    ax.set_title(f"{info['country']} {info['city']} {info['zip']}")
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')

    ax.set_aspect('equal')

    world.plot(ax=ax)

    ax.plot(float(info['lon']), float(info['lat']), 'rx', label='marker only', markersize=10, mew=2)

    fig.show()
        
