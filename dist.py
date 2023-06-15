from math import radians, sin, cos, sqrt, asin

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth's surface using the haversine formula.

    Arguments:
    lat1 -- latitude of the first point (in degrees)
    lon1 -- longitude of the first point (in degrees)
    lat2 -- latitude of the second point (in degrees)
    lon2 -- longitude of the second point (in degrees)

    Returns:
    The distance between the two points (in miles).
    """
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    radius = 6371  # Radius of the Earth in kilometers
    distance = c * radius

    return distance*0.621371

# Example usage
latitude1 = float(input("Enter latitude of the first point: "))
longitude1 = float(input("Enter longitude of the first point: "))
latitude2 = float(input("Enter latitude of the second point: "))
longitude2 = float(input("Enter longitude of the second point: "))

result = haversine_distance(latitude1, longitude1, latitude2, longitude2)
print("The distance between the two points is approximately {:.2f} miles.".format(result))
