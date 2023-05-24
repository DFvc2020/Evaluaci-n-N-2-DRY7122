import requests

def calcular_viaje(ciudad_origen, ciudad_destino):
    url = f"http://www.mapquestapi.com/directions/v2/route?key=V9I8fxotq6x7hMmc0Hl4XDwHyMCY5OCV&from={ciudad_origen}&to={ciudad_destino}&unit=k"
    response = requests.get(url)
    data = response.json()
    distancia = data["route"]["distance"]
    duracion = data["route"]["formattedTime"]
    return distancia, duracion

while True:
    ciudad_origen = input("Ingrese la ciudad de origen (o 'q' para salir): ")
    if ciudad_origen == 'q':
        break
    ciudad_destino = input("Ingrese la ciudad de destino (o 'q' para salir): ")
    if ciudad_destino == 'q':
        break
    distancia, duracion = calcular_viaje(ciudad_origen, ciudad_destino)
    print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia:.2f} kilómetros.")
    print(f"La duración del viaje es de {duracion}.")




