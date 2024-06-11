from concurrent import futures
import csv
import grpc

from Egepro_Protocol_Buffer_pb2 import EgaProRequest, EgaProResponse, EgaProIndexService

# Load data from CSV (replace with your actual logic)
egapro_data = {}
with open("index-egalite-fh-utf8.csv") as csvfile:
    reader = DictReader(csvfile, delimiter=";", quotechar='"')
    for row in reader:
        siren = row["SIREN"]
        if siren not in egapro_data:
            egapro_data[siren] = row
        elif egapro_data[siren]["Année"] < row["Année"]:
            egapro_data[siren].update(row)


class EgaProIndexService(EgaProIndexServiceServicer):

    def GetEgaProData(self, request, context):
        siren = request.siren
        response = egapro_data.get(siren)
        if response is None:
            return EgaProResponse(error="SIREN not found")
        else:
            data_message = EgaProData()
        for key, value in response.items():
            setattr(data_message, key, value)
            return EgaProResponse(data=data_message)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    EgaProIndexService.add_to_server(EgaProIndexService(), server)
    server.add_insecure_port("[::]:50051")  # Replace with your desired port
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
  serve()