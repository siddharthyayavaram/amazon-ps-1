import requests

"""
test data
        "id": 1,
        "length": 139.0,
        "breadth": 5.0,
        "height": 5.0,
        "mode": 2,
        "slot": 1.0,
        "days": 1.0,
        "lat1": 37.7749,
        "lon1": -122.4194,
        "lat2": 38.5816,
        "lon2": -121.4944
"""

def get_cost(id):
    url="http://127.0.0.1:8000/api/ships_list/"+str(id)+"/"
    response=requests.get(url)
    print(response.text)

def get_last_id():
    url="http://127.0.0.1:8000/api/ships_list/"
    response=requests.get(url)
    dat=response.json()
    max=-1
    for d in dat:
        if d["id"]>max:
            max=d["id"]
    return max

def add_data():
    url="http://127.0.0.1:8000/api/ships_list/"

    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    height = float(input("Enter the height: "))
    mode = int(input("Enter the mode: "))
    slot = float(input("Enter the slot: "))
    days = float(input("Enter the number of days: "))
    lat1 = float(input("Enter the latitude of point 1: "))
    lon1 = float(input("Enter the longitude of point 1: "))
    lat2 = float(input("Enter the latitude of point 2: "))
    lon2 = float(input("Enter the longitude of point 2: "))

    data = {
    "length": length,
    "breadth": breadth,
    "height": height,
    "mode": mode,
    "slot": slot,
    "days": days,
    "lat1": lat1,
    "lon1": lon1,
    "lat2": lat2,
    "lon2": lon2
}

    response = requests.post(url, data=data)
    response.raise_for_status()

add_data()
get_cost(get_last_id())
