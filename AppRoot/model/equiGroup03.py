import itertools

def generar_combinaciones_jugadores(jugadores,equiposAGenerar):
    """
    Este método utiliza la función combinations de la biblioteca itertools para generar todas las combinaciones posibles de jugadores tomando equiposAGenerar jugadores a la vez. Devuelve una lista de todas las combinaciones generadas.
    """
    return list(itertools.combinations(jugadores, equiposAGenerar))

def generar_equipos(combinaciones_jugadores):
    """
    Este método genera una lista de nombres de equipos utilizando una comprensión de lista. Cada nombre de equipo se forma concatenando la cadena "Equipo" con un número que va desde 1 hasta el número total de combinaciones de jugadores más 1
    """
    return [f'Equipo{i}' for i in range(1, len(combinaciones_jugadores) + 1)]

def calcular_peso_equipo(jugadores_equipo):
    """
    Este método calcula el peso total de un equipo sumando los valores de peso de cada jugador en el equipo. Recibe como entrada una lista de diccionarios de jugadores y devuelve un número entero que representa el peso total del equipo.
    """
    return sum(jugador['peso'] for jugador in jugadores_equipo)

def removePlayerDuplicados(jugadores_equipo1, jugadores_equipo2):
    """
    Elimina jugadores que pueden estar en ambos equipos a la vez.

    Este método verifica si hay algún jugador en común entre los dos equipos. Recibe como entrada dos listas de diccionarios de jugadores que representan los jugadores de cada equipo. Devuelve un valor booleano: True si no hay jugadores en común y False si hay al menos un jugador en común.
    """
    jugadores1_nombres = [jugador['nombre'] for jugador in jugadores_equipo1]
    jugadores2_nombres = [jugador['nombre'] for jugador in jugadores_equipo2]
    return not any(jugador_nombre in jugadores2_nombres for jugador_nombre in jugadores1_nombres)

def obtener_enfrentamientos(enfrentamientos, combinaciones_jugadores, equipos):
    """
    Este método recorre una lista de enfrentamientos y realiza las siguientes operaciones para cada enfrentamiento:

    Obtiene los jugadores de cada equipo en base a los nombres de los equipos.
    Verifica si el enfrentamiento es válido utilizando el método removePlayerDuplicados().
    Si el enfrentamiento es válido, calcula el peso de cada equipo utilizando el método calcular_peso_equipo().
    Agrega un nuevo elemento a lista_enfrentamientos que contiene los nombres de los equipos y los pesos de cada equipo.
    Devuelve la lista lista_enfrentamientos que contiene los enfrentamientos válidos.
    """
    lista_enfrentamientos = []
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2 = enfrentamiento
        jugadores_equipo1 = combinaciones_jugadores[equipos.index(equipo1)]
        jugadores_equipo2 = combinaciones_jugadores[equipos.index(equipo2)]

        if removePlayerDuplicados(jugadores_equipo1, jugadores_equipo2):
            peso_equipo1 = calcular_peso_equipo(jugadores_equipo1)
            peso_equipo2 = calcular_peso_equipo(jugadores_equipo2)
            lista_enfrentamientos.append((equipo1, equipo2, peso_equipo1, peso_equipo2))

    return lista_enfrentamientos

def aplicarUmbralEnfrentamiento(enfrentamientos, umbral):
    """
    filtra aquellos enfrentamientos que tengan el umbral de peso exigido
    """
    enfrentamientos_validos = []
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2, peso_equipo1, peso_equipo2 = enfrentamiento
        diferencia_peso = abs(peso_equipo1 - peso_equipo2)
        if diferencia_peso <= umbral:
            enfrentamientos_validos.append(enfrentamiento)
    return enfrentamientos_validos

def mostrar_enfrentamientos(enfrentamientos):
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2, peso_equipo1, peso_equipo2 = enfrentamiento
        print(f"{equipo1} (Peso: {peso_equipo1}) vs {equipo2} (Peso: {peso_equipo2})")


jugadores = [
    {'nombre': 'Jugador1', 'peso': 1, 'sexo': 'M'},
    {'nombre': 'Jugador2', 'peso': 2, 'sexo': 'M'},
    {'nombre': 'Jugador3', 'peso': 3, 'sexo': 'F'},
    {'nombre': 'Jugador4', 'peso': 4, 'sexo': 'F'},
    {'nombre': 'Jugador5', 'peso': 5, 'sexo': 'M'},
    {'nombre': 'Jugador6', 'peso': 6, 'sexo': 'M'},
]
equiposAGenerar=3
umbral=2
combinaciones_jugadores = generar_combinaciones_jugadores(jugadores,equiposAGenerar)
equipos = generar_equipos(combinaciones_jugadores)

#generamos todas las combinaciones de los enfrentamientos
enfrentamientos = list(itertools.combinations(equipos, 2))
print("Sin filtro")
print(enfrentamientos)


#filtramos aquellos enfrentamientos con jugadores en ambos equipos
enfrentamientos = obtener_enfrentamientos(enfrentamientos, combinaciones_jugadores, equipos)
print("Filtro jugadores duplicados")
mostrar_enfrentamientos(enfrentamientos)

#filtramos aquellos enfrentamientos con umbral no permitido
enfrentamientos_validos = aplicarUmbralEnfrentamiento(enfrentamientos, umbral)
print("Filtro umbral")
mostrar_enfrentamientos(enfrentamientos_validos)
