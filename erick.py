import urllib.request
import json


def get_lat_long_from_location(location):
    suggest_uri = ("https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/suggest"
                   "?f=json&countryCode=USA%2CPRI%2CVIR%2CGUM%2CASM"
                   "&category=Land+Features%2CBay%2CChannel%2CCove%2CDam%2CDelta%2CGulf%2CLagoon%2CLake%2COcean%2CReef"
                   "%2CReservoir%2CSea%2CSound%2CStrait%2CWaterfall%2CWharf%2CAmusement+Park%2CHistorical+Monument"
                   "%2CLandmark%2CTourist+Attraction%2CZoo%2CCollege%2CBeach%2CCampground%2CGolf+Course%2CHarbor%2CNature"
                   "+Reserve%2COther+Parks+and+Outdoors%2CPark%2CRacetrack%2CScenic+Overlook%2CSki+Resort%2CSports+Center"
                   "%2CSports+Field%2CWildlife+Reserve%2CAirport%2CFerry%2CMarina%2CPier%2CPort%2CResort%2CPostal"
                   "%2CPopulated+Place"
                   "&maxSuggestions=5"
                   "&text={}".format(location.replace(" ", "%20")))
    suggest_results = json.loads(urllib.request.urlopen(suggest_uri).read())
    first_suggestion = suggest_results['suggestions'][0]
    magic_key = first_suggestion['magicKey']
    location = first_suggestion['text']

    print("Top Match: {}".format(location))
    lat_long_req_uri = (
        "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find?text={}&magicKey={}&f=json".format(
            location, magic_key)).replace(" ", "%20")
    find_results = json.loads(urllib.request.urlopen(lat_long_req_uri).read())

    return_results = dict()
    return_results["lat"] = find_results['locations'][0]['feature']['geometry']['y']
    return_results["long"] = find_results['locations'][0]['feature']['geometry']['x']
    return return_results


def get_forecast_for_lat_long(lat, long):
    forecast_uri = ("https://forecast.weather.gov/MapClick.php?&lat={}&lon={}&FcstType=json".format(lat, long))
    forecast_results = json.loads(urllib.request.urlopen(forecast_uri).read())
    return forecast_results["data"]


def get_forecast():
    location = input("Location: ")
    lat_long = get_lat_long_from_location(location)
    forecast = get_forecast_for_lat_long(lat_long["lat"], lat_long["long"])
    print("Current forecast: {}F, {}".format(forecast["temperature"][0], forecast["weather"][0]))
    print("Any other locations you want to lookup?")
    return get_forecast()


def main():
    print("Let's pull the current forecast!")
    get_forecast()


main()
