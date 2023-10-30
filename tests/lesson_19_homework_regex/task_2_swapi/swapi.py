import requests
import json

url_ship = "https://swapi.dev/api/starships/?search=Millennium Falcon"

response_ship = requests.get(url_ship)

if response_ship.status_code == 200:
    data_ship = response_ship.json().get("results", [])[0]

    ship_info = {
        "name": data_ship["name"],
        "max speed in atmosphere": data_ship["max_atmosphering_speed"],
        "class": data_ship["starship_class"],
        "pilots": []
    }

    for pilot_url in data_ship["pilots"]:
        pilot_response = requests.get(pilot_url)
        if pilot_response.status_code == 200:
            pilot_data = pilot_response.json()
            planet_url = pilot_data["homeworld"]

            planet_response = requests.get(planet_url)
            if planet_response.status_code == 200:
                planet_data = planet_response.json()
                pilot_info = {
                    "pilot name": pilot_data["name"],
                    "height": pilot_data["height"],
                    "weight": pilot_data["mass"],
                    "Homeworld name": planet_data["name"],
                    "Link to homeworld": planet_url
                }
                ship_info["pilots"].append(pilot_info)

    with open("millennium_falcon.json", "w") as json_file:
        json.dump(ship_info, json_file, indent=4)
