import csv
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

# Chemin vers le fichier CSV
csv_file_path = "./database.csv"

# Modèle de données pour une entreprise
class Entreprise:
    def __init__(self, siren, denomination, adresse):
        self.siren = siren
        self.denomination = denomination
        self.adresse = adresse

    def to_dict(self):
        return {
            "Siren": self.siren,
            "Raison Sociale": self.denomination,
            "Departement": self.adresse,
        }

# Fonction pour charger les données du CSV
def load_entreprises_from_csv(file_path):
    entreprises = {}
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            entreprises[row["SIREN"]] = Entreprise(
                row["SIREN"], row["Raison Sociale"], row["Département"]
            )
    return entreprises

entreprises = load_entreprises_from_csv(csv_file_path)

# Ressource pour récupérer une entreprise par SIREN
class EntrepriseResource(Resource):
    def get(self, siren):
        if siren in entreprises:
            return jsonify(entreprises[siren].to_dict())
        else:
            return jsonify({"message": "Entreprise non trouvée"}), 404

# Ajout de la ressource à l'API
api.add_resource(EntrepriseResource, "/entreprises/<string:siren>")

if __name__ == "__main__":
    app.run(debug=True)
