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