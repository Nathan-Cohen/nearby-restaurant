import keyword
import random
import requests
from geopy.geocoders import Nominatim

def geocoder_adresse(adresse):
    geolocator = Nominatim(user_agent="nearby_restaurant")
    location = geolocator.geocode(adresse)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        print("L'adresse n'a pas pu être géocodée.")
        return None, None

def recherche_lieu_google_places():
    adresse = input("Entrez une adresse : ")
    latitude, longitude = geocoder_adresse(adresse)
    print(latitude, longitude)

    if latitude is not None and longitude is not None:
        radius = 600
        lieu_type = "restaurant"
        keyword = "bakery|restaurant|italian|turkish|japanese|french|thai|mexican|fast_food|pizza|sushi|burger|kebab"
        api_key = "YOUR_API_KEY"

        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={keyword}&location={latitude},{longitude}&radius={radius}&type={lieu_type}&key={api_key}&maxprice=3"

        all_results = []  # Pour stocker tous les résultats

        while True:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                # Filtrer les résultats pour ne conserver que les restaurants à emporter
                has_takeaway = [place for place in results if any('takeaway' in restaurant_type for restaurant_type in place.get('types', []))]

                all_results.extend(has_takeaway)

                # Vérifiez si une page suivante existe
                next_page_token = data.get("next_page_token")

                if next_page_token:
                    # Attendez quelques secondes avant de faire la prochaine requête
                    import time
                    time.sleep(2)

                    # Utilisez le token pour obtenir la page suivante
                    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&type={lieu_type}&key={api_key}&pagetoken={next_page_token}&results_per_page=100"
                else:
                    break
            else:
                print("La requête a échoué avec le code d'état :", response.status_code)
                break

        return all_results

def restaurants_ouverts(restaurants):
    open_restaurants = []

    for place in restaurants:
        if "opening_hours" in place:
            if place["opening_hours"].get("open_now", False):
                open_restaurants.append(place["name"])

    print(open_restaurants)
    return open_restaurants

def selectionner_restaurant_aleatoire(restaurants):
    if len(restaurants) == 0:
        print("Aucun restaurant ouvert n'a été trouvé.")
    else:
        restaurant_aleatoire = random.choice(restaurants)
        print("Restaurant sélectionné au hasard parmi les restaurants ouverts :")
        print(restaurant_aleatoire)

restaurants = recherche_lieu_google_places()
restaurants_ouverts_list = restaurants_ouverts(restaurants)
selectionner_restaurant_aleatoire(restaurants_ouverts_list)
