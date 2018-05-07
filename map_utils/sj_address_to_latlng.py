import json
import requests

maps_api_key = 'PUT YOURS HERE'
sj_zip_codes = [94089, 95002, 95008, 95013, 95014, 95032, 95035, 95037,
                95050, 95054, 95070, 95110, 95111, 95112, 95113, 95116,
                95117, 95118, 95119, 95120, 95121, 95122, 95123, 95124,
                95125, 95126, 95127, 95128, 95129, 95130, 95131, 95132,
                95133, 95134, 95135, 95136, 95138, 95139, 95140, 95148]

def CreateAddressLatLngRequest(address, postal):
    components_param = 'country:US,'
    components_param += '|' + 'locality:san+jose' + '|' + 'postal_code:' + postal
    address_param = 'address:' + address
    bounds_param = '37.387894,-121.966484|37.196050,-121.568630'
    request_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&components=%s&bounds=%s&key=%s' % (address, components_param, bounds_param, maps_api_key)
    return request_url

def ResultWithSanJoseLocation(response):
    for result in response.json()['results']:
        for component in result['address_components']:
            if component['long_name'] == 'San Jose':
                return result
    return None

def FindLatLngForAddress(address):
    for postal in sj_zip_codes:
        rurl = CreateAddressLatLngRequest(address, str(postal))
        response = requests.get(rurl)
        result = ResultWithSanJoseLocation(response)
        if result is not None:
            return result
    return {}
print(FindLatLngForAddress('50 KINGS ROW'))
