import requests

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

    time = float(input("Enter the time: "))
    zone = input("Enter the zone: ")
    weight = float(input("Enter the weight: "))
    carrier = input("Enter the carrier: ")

    data = {'time': time,'zone': zone,'weight': weight,'carrier': carrier}

    response = requests.post(url, data=data)
    response.raise_for_status()

add_data()
get_cost(get_last_id())
