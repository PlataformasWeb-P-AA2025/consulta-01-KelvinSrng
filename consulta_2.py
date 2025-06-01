from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["demo_base"]
coleccion = db["informacion_excel"]

print("Consulta 2: Partidos jugados en cancha dura (Hard)")

consulta = {"Surface": "Hard"}

for doc in coleccion.find(consulta).limit(25):
    print(f"{doc['Tournament']} | {doc['Winner']} vs {doc['Loser']} | Superficie: {doc['Surface']}")
