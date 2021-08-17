import tldextract
import socket
import requests
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


API_URL = "http://ip-api.com/json/" 


def information(string):

    try:

        socket.inet_aton(string)

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

            print(IP)

            if (info := requests.get(API_URL + IP).json() )['status'] == "success":
                return info
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}

        except:
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}
        


def plot_map(info):
    
    fig, ax = plt.subplots(figsize=(10,6))
    
    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    
    countries.plot(color="lightgrey", ax=ax)
    
    
    df = pd.DataFrame({'longitude':[info['lon']], 'latitude': [info['lat']]})
    
    df.plot(
        x="longitude", y="latitude", kind="scatter", colormap="YlOrRd", 
        title=f"{info['country']}, {info['city']}, {info['zip']}", ax=ax
    )

    # add grid
    ax.grid(b=True, alpha=0.5)
    plt.show() 

    
