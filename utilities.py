import tldextract
import socket
import requests


API_URL = "http://ip-api.com/json/" 

def information(string):

    try:

        socket.inet_aton(string)

        if((info := requests.get(API_URL + string).json() )['status'] == "success"):
            return info
        
        return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}

    except:

        try:

            extracted = tldextract.extract(string)

            IP = socket.gethostbyname(f'{extracted.domain}.{extracted.suffix}')

            if((info := requests.get(API_URL + string).json() )['status'] == "success"):
                return info
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}

        except:
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}
        
