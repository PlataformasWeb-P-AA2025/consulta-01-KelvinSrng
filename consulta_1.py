from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["demo_base"]
coleccion = db["informacion_excel"]

print("Consulta 1: Ganadores con ranking menor a 50")

consulta = {"WRank": {"$lt": 50}}

for doc in coleccion.find(consulta).limit(5):
    print(f"{doc['Winner']} vs {doc['Loser']} | WRank: {doc['WRank']} | Resultado: {doc['Wsets']}-{doc['Lsets']}")