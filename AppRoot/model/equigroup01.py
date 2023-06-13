import itertools

jugadores = [
    {'nombre': 'Jugador1', 'peso': 1},
    {'nombre': 'Jugador2', 'peso': 2},
    {'nombre': 'Jugador3', 'peso': 3},
    {'nombre': 'Jugador4', 'peso': 4},
    {'nombre': 'Jugador5', 'peso': 5},
    {'nombre': 'Jugador6', 'peso': 6},
]

combinaciones_jugadores = list(itertools.combinations(jugadores, 3))
print("combinaciones_jugadores:")
print(combinaciones_jugadores)
#---------------------------------
#impresión
i=0;
for i, combinacion in enumerate(combinaciones_jugadores, 1):
    print(f"Equipo {i}: {combinacion}")

print(f"{len(combinaciones_jugadores)} Equipo encontrados")
#---------------------------------

equipos = [f'Equipo{i}' for i in range(1, len(combinaciones_jugadores) + 1)]
print("equipos")
print(equipos,type(equipos))
print("equipo.index(0)")
print(equipos.index("Equipo1"))

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
        peso_equipo1 = sum(jugador['peso'] for jugador in jugadores_equipo1)
        peso_equipo2 = sum(jugador['peso'] for jugador in jugadores_equipo2)
        print(f"{equipo1} (Peso: {peso_equipo1}) vs {equipo2} (Peso: {peso_equipo2})")
