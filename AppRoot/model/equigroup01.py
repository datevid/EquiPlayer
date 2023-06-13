import itertools

jugadores = [
    {'nombre': 'Jugador1', 'peso': 1},
    {'nombre': 'Jugador2', 'peso': 2},
    {'nombre': 'Jugador3', 'peso': 3},
    {'nombre': 'Jugador4', 'peso': 4},
]

combinaciones_jugadores = list(itertools.combinations(jugadores, 2))
#---------------------------------
#impresión
i=0;
for i, combinacion in enumerate(combinaciones_jugadores, 1):
    print(f"Equipo {i}: {combinacion}")

print(f"{len(combinaciones_jugadores)} Equipo encontrados")
#---------------------------------

equipos = [f'Equipo{i}' for i in range(1, len(combinaciones_jugadores) + 1)]
print("equipos")
print(equipos)

enfrentamientos = list(itertools.combinations(equipos, 2))
print("enfrentamientos")
print(enfrentamientos)

for enfrentamiento in enfrentamientos:
    equipo1, equipo2 = enfrentamiento
    jugadores_equipo1 = combinaciones_jugadores[equipos.index(equipo1)]
    jugadores_equipo2 = combinaciones_jugadores[equipos.index(equipo2)]
    
    jugadores1_nombres = [jugador['nombre'] for jugador in jugadores_equipo1]
    jugadores2_nombres = [jugador['nombre'] for jugador in jugadores_equipo2]
    
    #si algún jugador del equipo 1 está presente en el equipo 2
    if not any(jugador_nombre in jugadores2_nombres for jugador_nombre in jugadores1_nombres):
        print(f"{equipo1} vs {equipo2}")
