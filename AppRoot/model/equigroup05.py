import itertools
import random

"""
Este método utiliza la función combinations de la biblioteca itertools para generar todas las combinaciones posibles de jugadores tomando equiposAGenerar jugadores a la vez. Devuelve una lista de todas las combinaciones generadas.
"""
def generar_combinaciones_jugadores(jugadores,equiposAGenerar):
    return list(itertools.combinations(jugadores, equiposAGenerar))

"""
Asigna nombres a cada combinacion de jugadores
"""
def generarNombresEquipo(equiposPlayer):
    return [f'Equipo{i}' for i in range(1, len(equiposPlayer) + 1)]

"""
Muestra los jugadores por cada equipo.
"""
def mostrar_jugadores_por_equipo(equiposPlayer, equiposIndex):
    for i, equipo in enumerate(equiposIndex):
        jugadores_equipo = equiposPlayer[i]
        print(f"{equipo}:")
        for jugador in jugadores_equipo:
            print(f"Nombre: {jugador['nombre']}, Peso: {jugador['peso']}, Sexo: {jugador['sexo']}")
        print()

"""
Este método calcula el peso total de un equipo sumando los valores de peso de cada jugador en el equipo. Recibe como entrada una lista de diccionarios de jugadores y devuelve un número entero que representa el peso total del equipo.
"""
def calcular_peso_equipo(jugadores_equipo):
    return sum(jugador['peso'] for jugador in jugadores_equipo)

"""
Elimina jugadores que pueden estar en ambos equipos a la vez.
"""
def removePlayerDuplicados(jugadores_equipo1, jugadores_equipo2):
    jugadores1_nombres = [jugador['nombre'] for jugador in jugadores_equipo1]
    jugadores2_nombres = [jugador['nombre'] for jugador in jugadores_equipo2]
    return not any(jugador_nombre in jugadores2_nombres for jugador_nombre in jugadores1_nombres)

"""
Genera todos los enfrentamientos posibles a partir de las combinaciones de jugadores.
"""
def generar_enfrentamientos(equiposPlayer, equiposIndex):
    enfrentamientos = list(itertools.combinations(equiposIndex, 2))

    lista_enfrentamientos = []
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2 = enfrentamiento
        jugadores_equipo1 = equiposPlayer[equiposIndex.index(equipo1)]
        jugadores_equipo2 = equiposPlayer[equiposIndex.index(equipo2)]

        peso_equipo1 = calcular_peso_equipo(jugadores_equipo1)
        peso_equipo2 = calcular_peso_equipo(jugadores_equipo2)
        lista_enfrentamientos.append((equipo1, equipo2, peso_equipo1, peso_equipo2))

    return lista_enfrentamientos

"""
Elimina los enfrentamientos que contienen jugadores duplicados en ambos equipos.
elimina los jugadores duplicados en los enfrentamientos.
"""
def eliminar_jugadores_duplicados(enfrentamientos,equiposPlayer, equiposIndex):
    
    enfrentamientos_validos = []
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2, peso_equipo1, peso_equipo2 = enfrentamiento
        jugadores_equipo1 = equiposPlayer[equiposIndex.index(equipo1)]
        jugadores_equipo2 = equiposPlayer[equiposIndex.index(equipo2)]

        if removePlayerDuplicados(jugadores_equipo1, jugadores_equipo2):
            #print("Enfrentamiento aceptado")
            peso_equipo1 = calcular_peso_equipo(jugadores_equipo1)
            peso_equipo2 = calcular_peso_equipo(jugadores_equipo2)
            enfrentamientos_validos.append((equipo1, equipo2, peso_equipo1, peso_equipo2))
        else:
            #print("Enfrentamiento removido -> invalidado")
            pass

    return enfrentamientos_validos


"""
filtra aquellos enfrentamientos que tengan el umbral de peso exigido
"""
def aplicarUmbralEnfrentamiento(enfrentamientos, umbralPesoXEquipo):
    enfrentamientos_validos = []
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2, peso_equipo1, peso_equipo2 = enfrentamiento
        diferencia_peso = abs(peso_equipo1 - peso_equipo2)
        if diferencia_peso <= umbralPesoXEquipo:
            enfrentamientos_validos.append(enfrentamiento)
    return enfrentamientos_validos

def mostrar_enfrentamiento(enfrentamiento):
    equipo1, equipo2, peso_equipo1, peso_equipo2 = enfrentamiento
    print(f"{equipo1} (Peso: {peso_equipo1}) vs {equipo2} (Peso: {peso_equipo2})")

def mostrar_enfrentamientos(enfrentamientos):
    for enfrentamiento in enfrentamientos:
        mostrar_enfrentamiento(enfrentamiento)

def obtener_enfrentamiento_aleatorio(enfrentamientos_validos):
    return random.choice(enfrentamientos_validos)

def obtener_jugadores_enfrentamiento(enfrentamiento, equiposPlayer, equiposIndex):
    equipo1, equipo2, peso_equipo1, peso_equipo2 = enfrentamiento
    jugadores_equipo1 = equiposPlayer[equiposIndex.index(equipo1)]
    jugadores_equipo2 = equiposPlayer[equiposIndex.index(equipo2)]
    return jugadores_equipo1, jugadores_equipo2

def showTeamData(team):
    for player in team:
        print(f"Nombre: {player['nombre']}, Peso: {player['peso']}, Sexo: {player['sexo']}")


def matchPlayers(jugadores,equiposAGenerar):
    print("jugadores")
    print(jugadores)
    
    equiposPlayer = generar_combinaciones_jugadores(jugadores,equiposAGenerar)
    equiposIndex = generarNombresEquipo(equiposPlayer)
    print("equiposIndex")
    print(equiposIndex)
    mostrar_jugadores_por_equipo(equiposPlayer,equiposIndex)

    #Obtiene los enfrentamientos de todas las combinaciones de jugadores
    enfrentamientos = generar_enfrentamientos(equiposPlayer, equiposIndex)
    #print("Sin filtro")
    #mostrar_enfrentamientos(enfrentamientos)

    #filtramos aquellos enfrentamientos con jugadores que se encuentran en ambos equipos
    enfrentamientos_validos=eliminar_jugadores_duplicados(enfrentamientos,equiposPlayer,equiposIndex)
    print("Filtro jugadores duplicados")
    mostrar_enfrentamientos(enfrentamientos_validos)

    #filtramos aquellos enfrentamientos con umbral no permitido
    enfrentamientos_validos = aplicarUmbralEnfrentamiento(enfrentamientos_validos, umbralPesoXEquipo)
    print(f"Filtro con umbral de peso total por equipo: {umbralPesoXEquipo}")
    mostrar_enfrentamientos(enfrentamientos_validos)

    #obtenemos un solo enfrentamiento de los que quedaron
    enfrentamiento_aleatorio = obtener_enfrentamiento_aleatorio(enfrentamientos_validos)
    print("Enfrentamiento aleatorio:")
    mostrar_enfrentamiento(enfrentamiento_aleatorio)

    #obtenemos los jugadores del enfrentamiento
    jugadores_equipo1, jugadores_equipo2 = obtener_jugadores_enfrentamiento(enfrentamiento_aleatorio, equiposPlayer, equiposIndex)

    return jugadores_equipo1,jugadores_equipo2

jugadores = [
    {'nombre': 'Jugador1', 'peso': 1, 'sexo': 'M'},
    {'nombre': 'Jugador2', 'peso': 2, 'sexo': 'M'},
    {'nombre': 'Jugador3', 'peso': 3, 'sexo': 'F'},
    {'nombre': 'Jugador4', 'peso': 4, 'sexo': 'F'},
    {'nombre': 'Jugador5', 'peso': 5, 'sexo': 'M'},
    {'nombre': 'Jugador6', 'peso': 6, 'sexo': 'M'},
]
equiposAGenerar=3
umbralPesoXEquipo=1
jugadores_equipo1, jugadores_equipo2=matchPlayers(jugadores,equiposAGenerar)
print("Jugadores del equipo 1:")
showTeamData(jugadores_equipo1)

print("Jugadores del equipo 2:")
showTeamData(jugadores_equipo2)
