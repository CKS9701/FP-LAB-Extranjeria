import csv
from typing import NamedTuple

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)

def lee_datos_extranjeria(ruta_fichero: str) -> list[RegistroExtranjeria]:
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)

        datos = []

        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            distrito = distrito.strip()
            seccion = seccion.strip()
            barrio = barrio.strip()
            pais = pais.strip()
            hombres = int(hombres)
            mujeres = int(mujeres)

            datos.append(RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres))

        return datos
    
    
def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria 
    y devuelve el número de nacionalidades distintas presentes 
    en los registros de la lista recibida como parámetro.'''

    paises = set()
    for dato in registros:
        paises.add(dato.pais)

    return len(paises)


def secciones_distritos_con_extranjeros_nacionalidades(registros: list[RegistroExtranjeria], paises: set[str]) -> list[tuple[str,str]]: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria 
    y un conjunto de cadenas con nombres de países, y devuelve 
    una lista de tuplas (distrito, seccion) con los distritos y 
    secciones en los que hay extranjeros del conjunto de paises 
    dado como parámetro. La lista de tuplas devuelta estará ordenada por distrito.'''

    ret = []

    for dato in registros:
        if dato.pais in paises:
            ret.append((dato.distrito, dato.seccion))

    ret.sort()

    return ret


def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str:int]: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria 
    y devuelve un diccionario de tipo {str:int} en el que las 
    claves son los países y los valores son el número total de 
    extranjeros (tanto hombres como mujeres) de cada país.'''

    ret = dict()
    for dato in registros:
        if dato.pais in ret:
            ret[dato.pais] += dato.hombres + dato.mujeres
        else:
            ret[dato.pais] = dato.hombres + dato.mujeres
        
    return ret


def top_n_extranjeria(registros: list[RegistroExtranjeria], n: int = 3) -> list[tuple[str,int]]: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve una lista de tuplas (pais, numero_extranjeros) con 
    los n países de los que hay más población extranjera en los 
    registros pasados como parámetros.'''

    paises_poblacion = total_extranjeros_por_pais(registros)
    mas_poblacion = [(poblacion, pais) for (pais, poblacion) in paises_poblacion.items()]
    mas_poblacion.sort(reverse=True)

    ret = []
    for i in range(0, n):
        pais, poblacion = mas_poblacion[i][1], mas_poblacion[i][0]
        ret.append((pais, poblacion))

    return ret


def barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> str: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve el nombre del barrio en el que hay un mayor número 
    de países de procedencia distintos.'''

    paises_max = 0
    barrio_max = ""

    paises_barrio = dict()
    for dato in registros:
        if dato.barrio in paises_barrio:
            paises_barrio[dato.barrio] += 1
        else:
            paises_barrio[dato.barrio] = 1


    for barrio, paises in paises_barrio.items():
        if paises > paises_max:
            paises_max = paises
            barrio_max = barrio

    return barrio_max


def barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo: str = None) -> str: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve el nombre del barrio en el que hay un mayor número 
    de extranjeros, bien sea en total (tanto hombres como mujeres) 
    si tipo tiene el valor None, bien sea de hombres si tipo es 
    'Hombres', o de mujeres si tipo es 'Mujeres'.'''

    if tipo is None:
        return top_n_extranjeria(registros, 1)[0][0]
    else:
        personas_barrio = dict()
        for dato in registros:
            if tipo == 'Hombres':
                if dato.barrio in personas_barrio:
                    personas_barrio[dato.barrio] += dato.hombres
                else:
                    personas_barrio[dato.barrio] = dato.hombres

            elif tipo == 'Mujeres':
                if dato.barrio in personas_barrio:
                    personas_barrio[dato.barrio] += dato.mujeres
                else:
                    personas_barrio[dato.barrio] = dato.mujeres

        
        personas_max = 0
        barrio_max = ""

        for barrio, personas in personas_barrio.items():
            if personas > personas_max:
                personas_max = personas
                barrio_max = barrio
        
        return barrio_max


def pais_mas_representado_por_distrito(registros: list[RegistroExtranjeria]) -> dict[str,str]: 
    '''recibe una lista de tuplas de tipo RegistroExtranjeria y 
    devuelve un diccionario de tipo {str:str} en el que las claves 
    son los distritos y los valores los países de los que hay más 
    extranjeros residentes en cada distrito.'''

    personas_paises_distrito: dict[str,dict[str,int]] = dict()

    for dato in registros:
        if dato.distrito in personas_paises_distrito:
            if dato.pais in personas_paises_distrito[dato.distrito]:
                personas_paises_distrito[dato.distrito][dato.pais] += dato.hombres + dato.mujeres
            else:
                personas_paises_distrito[dato.distrito][dato.pais] = dato.hombres + dato.mujeres
        else:
            personas_paises_distrito[dato.distrito] = dict()
            personas_paises_distrito[dato.distrito][dato.pais] = dato.hombres + dato.mujeres
        

    ret = dict()

    for distrito, personas_paises in personas_paises_distrito.items():
        personas_max = 0
        pais_max = ""
        for pais, personas in personas_paises.items():
            if personas > personas_max:
                personas_max = personas
                pais_max = pais
        
        ret[distrito] = pais_max

    return ret