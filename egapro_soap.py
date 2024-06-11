from csv import DictReader
from flask import Flask, request
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import AnyDict

# Read the index-egalite-fh.csv file and store it in a dictionary
egapro_data = {}

with open("index-egalite-fh-utf8.csv", encoding="utf-8") as csv:
    reader = DictReader(csv, delimiter=";", quotechar='"')
    for row in reader:
        if egapro_data.get(row["SIREN"]) is None:
            egapro_data[row["SIREN"]] = row
        elif egapro_data[row["SIREN"]]["Année"] < row["Année"]:
            egapro_data[row["SIREN"]].update(row)

# Define a Spyne service
class EgaProService(ServiceBase):
    @rpc(Integer, _returns=AnyDict)
    def get_siren(ctx, siren):
        """
        Return the EgaPro data for a given SIREN number.
        A 404 is returned if the SIREN is not found.
        """
        response = egapro_data.get(str(siren))
        if response is None:
            return {"error": "SIREN not found"}
        else:
            return response

# Create Flask application
flask_app = Flask(__name__)

# Create the Spyne application
soap_app = Application(
    [EgaProService],
    tns='spyne.examples.flask',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Wrap the Spyne application with the Wsgi application
wsgi_app = WsgiApplication(soap_app)

# Mount the WSGI application inside Flask
@flask_app.route("/soap", methods=['POST'])
def soap():
    return wsgi_app(request.environ, request.start_response)

# A debug flask launcher
if __name__ == "__main__":
    flask_app.run(debug=True)
