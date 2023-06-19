import itertools
import random
import time

"""
get_combinaciones_jugadores_teams(jugadores, equiposTotal): Esta función utiliza la función combinations del módulo itertools para generar todas las combinaciones posibles de jugadores tomando equiposTotal jugadores a la vez. Devuelve una lista de todas las combinaciones generadas.
"""
def get_combinaciones_jugadores_teams(jugadores, equiposTotal):
    return list(itertools.combinations(jugadores, equiposTotal))


"""
Asigna nombres a cada combinacion de jugadores
getTeamsIndex(equiposPlayer): Esta función asigna nombres a cada combinación de jugadores. Recibe una lista de equipos y devuelve una lista de nombres de equipos.
"""


def getTeamsIndex(equiposPlayer):
    return [f'Equipo{i}' for i in range(1, len(equiposPlayer) + 1)]


"""
Muestra los jugadores por cada equipo.
mostrar_jugadores_por_equipo(equiposPlayer, equiposIndex): Esta función muestra los jugadores por cada equipo. Recibe una lista de equipos y una lista de nombres de equipos, y muestra los jugadores de cada equipo en el formato especificado.
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

calcular_peso_equipo(team): Esta función calcula el peso total de un equipo sumando los valores de peso de cada jugador en el equipo. Recibe como entrada una lista de diccionarios de jugadores y devuelve un número entero que representa el peso total del equipo.
"""


def calcular_peso_equipo(team):
    return sum(jugador['peso'] for jugador in team)


"""
Elimina jugadores que pueden estar en ambos equipos a la vez.
Determina si un jugador está repetido en los demás teams

ifPlayerRepeat(enfrentamiento): Esta función verifica si hay jugadores repetidos en los equipos de un enfrentamiento. Recibe un enfrentamiento (una lista de equipos) y devuelve True si hay jugadores repetidos y False en caso contrario.
"""


def ifPlayerRepeat(enfrentamiento):
    jugadores = set()  # Conjunto para almacenar los índices de jugadores

    # Iterar sobre cada equipo en el enfrentamiento
    for equipo in enfrentamiento:
        for jugadorIndex in equipo:
            # Verificar si el índice de jugador ya está en el conjunto "jugadores"
            if jugadorIndex in jugadores:
                return True  # Si el índice de jugador se repite, retornar True
            jugadores.add(jugadorIndex)  # Agregar el índice de jugador al conjunto

    return False  # Si no se encontraron repeticiones, retornar False


"""
getTeamMeta(teamIndex, playersAll): Esta función devuelve una lista de diccionarios de jugadores correspondiente a un equipo en base a su índice en la lista de jugadores completa.
"""
def getTeamMeta(teamIndex, playersAll):
    teamMeta = []
    for playerIndex in teamIndex:
        player = playersAll[playerIndex]
        teamMeta.append(player)
    return teamMeta;


"""
Genera todos los enfrentamientos posibles a partir de las combinaciones de jugadores.

generar_enfrentamientos(teamsIndex, nCombinations): Esta función genera todos los enfrentamientos posibles a partir de las combinaciones de equipos. Recibe una lista de índices de equipos y un número que representa la cantidad de equipos por enfrentamiento. Devuelve una lista de enfrentamientos.
"""


def generar_enfrentamientos(teamsIndex, nCombinations):
    enfrentamientos = list(itertools.combinations(teamsIndex, nCombinations))

    return enfrentamientos


"""
Elimina los enfrentamientos que contienen jugadores duplicados en ambos equipos.
elimina los jugadores duplicados en los enfrentamientos.

eliminar_jugadores_duplicados(enfrentamientos, players, teamsIndex): Esta función elimina los enfrentamientos que contienen jugadores duplicados en ambos equipos. Recibe una lista de enfrentamientos, la lista de jugadores y una lista de índices de equipos. Devuelve una lista de enfrentamientos válidos sin jugadores duplicados.
"""


def eliminar_jugadores_duplicados(enfrentamientos, players, teamsIndex):
    enfrentamientos_validos = []
    for enfrentamiento in enfrentamientos:
        if not ifPlayerRepeat(enfrentamiento):
            enfrentamientos_validos.append(enfrentamiento)
    return enfrentamientos_validos


"""
verifica umbra por team
donde sus elementos son los pesos de cada equipo
dataInput = [7, 14, 15]

verificar_diferencia_umbral(dataInput, umbral): Esta función verifica si la diferencia entre los elementos de una lista es menor o igual a un umbral dado. Recibe una lista de datos numéricos y un umbral. Devuelve True si la diferencia es menor o igual al umbral, y False en caso contrario.
"""


def verificar_diferencia_umbral(dataInput, umbral):
    for i in range(len(dataInput) - 1):
        for j in range(i + 1, len(dataInput)):
            diferencia = abs(dataInput[i] - dataInput[j])

            if diferencia > umbral:
                return False

    return True


"""
Obtiene el rendimiento de todo el enfrentamiento, es decir
obtiene los pesos de cada team y los devuelve en un array
enfrentamiento=(teamIndex1, teamIndex2, teamIndex3)
teamIndex=(4, 5)

getPerformanceEnfrentamiento(enfrentamiento, players): Esta función calcula el rendimiento de todo el enfrentamiento, es decir, los pesos de cada equipo. Recibe un enfrentamiento (una lista de equipos) y la lista de jugadores. Devuelve una lista de rendimientos de cada equipo.
"""


def getPerformanceEnfrentamiento(enfrentamiento, players):
    performanceTeamLst = []
    for teamIndex in enfrentamiento:
        performanceTeam = getPerformanceTeam(teamIndex, players)
        performanceTeamLst.append(performanceTeam)
    return performanceTeamLst;


"""
Obtiene el rendimiento por equipo
getPerformanceTeam(teamIndex, players): Esta función calcula el rendimiento de un equipo sumando los pesos de los jugadores en ese equipo. Recibe un índice de equipo y la lista de jugadores. Devuelve el rendimiento del equipo.
"""


def getPerformanceTeam(teamIndex, players):
    performanceTeam = 0;
    for playerIndex in teamIndex:
        player = players[playerIndex]
        performanceTeam = performanceTeam + player['peso']
    return performanceTeam;


"""
filtra aquellos enfrentamientos que tengan el umbral de peso exigido

aplicarUmbralEnfrentamiento(enfrentamientos, players, umbralPesoXEquipo): Esta función filtra los enfrentamientos que no cumplen con un umbral de peso exigido. Recibe una lista de enfrentamientos, la lista de jugadores y un umbral de peso por equipo. Devuelve una lista de enfrentamientos válidos que cumplen con el umbral.

"""


def aplicarUmbralEnfrentamiento(enfrentamientos, players, umbralPesoXEquipo):
    enfrentamientos_validos = []
    for enfrentamiento in enfrentamientos:
        performanceTeamEnfrentamiento = getPerformanceEnfrentamiento(enfrentamiento, players)
        umbralValid = verificar_diferencia_umbral(performanceTeamEnfrentamiento, umbralPesoXEquipo)
        if umbralValid:
            enfrentamientos_validos.append(enfrentamiento)
    return enfrentamientos_validos


"""
mostrar_enfrentamiento(enfrentamiento, players): Esta función muestra un enfrentamiento específico, mostrando los pesos de cada equipo. Recibe un enfrentamiento (una lista de equipos) y la lista de jugadores.
"""
def mostrar_enfrentamiento(enfrentamiento, players):
    print("Enfrentamiento:")
    for teamIndex in enfrentamiento:
        peso = getPerformanceTeam(teamIndex, players)
        print(f"Equipo {teamIndex}: Peso {peso}")
    print("===================")


"""
enfrentamiento=(teamIndex1, teamIndex2, teamIndex3)
teamIndex=(4, 5)

mostrar_enfrentamientos(enfrentamientos, players): Esta función muestra todos los enfrentamientos válidos, mostrando los pesos de cada equipo. Recibe una lista de enfrentamientos y la lista de jugadores.
"""


def mostrar_enfrentamientos(enfrentamientos, players):
    if len(enfrentamientos) > 0:
        for enfrentamiento in enfrentamientos:
            mostrar_enfrentamiento(enfrentamiento, players)


"""
getTeamsIndexRandom(enfrentamientos_validos): Esta función devuelve un enfrentamiento aleatorio de la lista de enfrentamientos válidos. Recibe una lista de enfrentamientos válidos.
"""
def getTeamsIndexRandom(enfrentamientos_validos):
    return random.choice(enfrentamientos_validos)


"""
getEnfrentamientoObj(enfrentamiento, players): Esta función devuelve los datos de jugadores correspondientes a un enfrentamiento específico. Recibe un enfrentamiento (una lista de equipos) y la lista de jugadores.
"""
def getEnfrentamientoObj(enfrentamiento, players):
    teamsSelected = []
    for teamIndex in enfrentamiento:
        teamMeta = getTeamMeta(teamIndex, players)
        teamsSelected.append(teamMeta)
    return teamsSelected


"""
showTeamsSelectedAndPlayers(teamXEnfrentamientoLst): Esta función muestra los equipos seleccionados y los jugadores correspondientes. Recibe una lista de equipos y jugadores.
"""
def showTeamsSelectedAndPlayers(teamXEnfrentamientoLst):
    print("teamsObjSelected:")
    if teamXEnfrentamientoLst:
        # recorremos el indice de cada equipo
        for team in teamXEnfrentamientoLst:
            print("Team:")
            for player in team:
                print(f"Nombre: {player['nombre']}, Peso: {player['peso']}, Sexo: {player['sexo']}")

"""
indexPlayers(players): Esta función devuelve una lista de índices de jugadores en base a la cantidad de jugadores. Recibe la lista de jugadores.
"""
def indexPlayers(players):
    playerIndexLst = []
    for i in range(len(players)):
        playerIndexLst.append(i)
    return playerIndexLst


"""
matchPlayers(players, totalTeams, umbralXEquipo): Esta función principal realiza todo el proceso de generar los enfrentamientos y filtrarlos según las restricciones de jugadores duplicados y umbral de peso. Recibe la lista de jugadores, la cantidad total de equipos y el umbral de peso por equipo. Devuelve una lista de equipos seleccionados.
"""
def matchPlayers(players, totalTeams,umbralXEquipo):
    playerIndexLst = indexPlayers(players)
    # print(playerIndexLst)
    totalPlayersXTeam = int(len(players) / totalTeams)

    teamsIndex = get_combinaciones_jugadores_teams(playerIndexLst, totalPlayersXTeam)

    # Obtiene los enfrentamientos de todas las combinaciones de jugadores
    enfrentamientos = generar_enfrentamientos(teamsIndex, totalTeams)
    print(f"Sin filtro: {len(enfrentamientos)}")

    # filtramos aquellos enfrentamientos con jugadores que se encuentran en ambos equipos
    enfrentamientos_validos = eliminar_jugadores_duplicados(enfrentamientos, players, teamsIndex)
    print(f"Filtro jugadores duplicados: {len(enfrentamientos_validos)}")

    # filtramos aquellos enfrentamientos con umbral no permitido
    enfrentamientos_validos = aplicarUmbralEnfrentamiento(enfrentamientos_validos, players, umbralXEquipo)
    print(f"Filtro con umbral {umbralXEquipo}. Encontrados: {len(enfrentamientos_validos)}")
    if len(enfrentamientos_validos) == 0:
        print("no se obtuvieron enfrentamientos con umbral permitido")
        return None;
    else:
        mostrar_enfrentamientos(enfrentamientos_validos, players)

        # obtenemos un solo enfrentamiento de los que quedaron
        enfrentamientoSelected = getTeamsIndexRandom(enfrentamientos_validos)
        print("enfrentamientoSelected:")
        mostrar_enfrentamiento(enfrentamientoSelected, players)

        # obtenemos los jugadores del enfrentamiento
        enfrentamientoObj = getEnfrentamientoObj(enfrentamientoSelected, players)

        return enfrentamientoObj

def main():
    players = [
        {'nombre': 'Jugador1', 'peso': 1, 'sexo': 'M'},
        {'nombre': 'Jugador2', 'peso': 2, 'sexo': 'M'},
        {'nombre': 'Jugador3', 'peso': 3, 'sexo': 'F'},
        {'nombre': 'Jugador4', 'peso': 4, 'sexo': 'F'},
        {'nombre': 'Jugador5', 'peso': 5, 'sexo': 'M'},
        {'nombre': 'Jugador6', 'peso': 6, 'sexo': 'M'},
        {'nombre': 'Jugador7', 'peso': 7, 'sexo': 'M'},
        {'nombre': 'Jugador8', 'peso': 8, 'sexo': 'M'},
        {'nombre': 'Jugador9', 'peso': 9, 'sexo': 'M'},
    ]
    totalTeams = 3
    umbralXEquipo = 1

    # Medir el tiempo de ejecución
    start_time = time.time()
    teamsObjSelected = matchPlayers(players, totalTeams,umbralXEquipo)
    showTeamsSelectedAndPlayers(teamsObjSelected)
    end_time = time.time()
    # Calcular el tiempo transcurrido
    execution_time = end_time - start_time
    print("Tiempo de ejecución:", execution_time, "segundos")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
