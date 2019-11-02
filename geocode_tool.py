from arcgis.geocoding import geocode
from arcgis.gis import GIS
gis = GIS()

def geocode_address_executor(address):
    """
    Geocodes the given address and returns the first result back
    :param address:
    :return:
    """

    return geocode(address)[0]
