import itertools

def generar_combinaciones_jugadores(jugadores,equiposAGenerar):
    return list(itertools.combinations(jugadores, equiposAGenerar))

def generar_equipos(combinaciones_jugadores):
    return [f'Equipo{i}' for i in range(1, len(combinaciones_jugadores) + 1)]

def calcular_peso_equipo(jugadores_equipo):
    return sum(jugador['peso'] for jugador in jugadores_equipo)

def validar_enfrentamiento(jugadores_equipo1, jugadores_equipo2):
    jugadores1_nombres = [jugador['nombre'] for jugador in jugadores_equipo1]
    jugadores2_nombres = [jugador['nombre'] for jugador in jugadores_equipo2]
    return not any(jugador_nombre in jugadores2_nombres for jugador_nombre in jugadores1_nombres)

def mostrar_enfrentamientos(enfrentamientos, combinaciones_jugadores, equipos):
    for enfrentamiento in enfrentamientos:
        equipo1, equipo2 = enfrentamiento
        jugadores_equipo1 = combinaciones_jugadores[equipos.index(equipo1)]
        jugadores_equipo2 = combinaciones_jugadores[equipos.index(equipo2)]

        if validar_enfrentamiento(jugadores_equipo1, jugadores_equipo2):
            peso_equipo1 = calcular_peso_equipo(jugadores_equipo1)
            peso_equipo2 = calcular_peso_equipo(jugadores_equipo2)
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
combinaciones_jugadores = generar_combinaciones_jugadores(jugadores,equiposAGenerar)
equipos = generar_equipos(combinaciones_jugadores)
enfrentamientos = list(itertools.combinations(equipos, 2))

mostrar_enfrentamientos(enfrentamientos, combinaciones_jugadores, equipos)
