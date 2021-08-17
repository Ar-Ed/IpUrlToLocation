import tldextract
import socket
import requests

def information(string):

    try:
        
        socket.inet_aton(string)

        info = requests.get("http://ip-api.com/json/" + string).json()
        return info

    except:

        try:

            extracted = tldextract.extract(string)

            IP = socket.gethostbyname(f'{extracted.domain}.{extracted.suffix}')

            info = requests.get("http://ip-api.com/json/" + IP).json()

            print(info['country'], info['regionName'], info['city'], info['zip'], info['isp'], info['query'], info['lat'],info[ 'lon'])

            return info

        except:
            
            return {'country':'', 'city':'', 'zip': '', 'city': '', 'isp': '', 'lat': '', 'lon': '', 'query':''}
        