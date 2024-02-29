import requests
import json
def get_transport_data(start_date, end_date):
    # URL de l'API OpenGOV
    endpoint_url = "https://exemple.com/api/transport_data"
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'station': 'saint-lazare'
    }
    try:
        # Faites la requête à l'API
        response = requests.get(endpoint_url, params=params)
        # Vérifiez si la requête a réussi (code 200)
        if response.status_code == 200:
            # Récupérez les données JSON de la réponse
            return response.json()
        else:
            # Affichez un message d'erreur si la requête a échoué
            print(f"Erreur de requête : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")
        return None
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

