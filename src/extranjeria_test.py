from extranjeria import *

def test_lee_datos_extranjeria(ruta_fichero: str) -> None:
    print("Probando lee_datos_extranjeria()...")

    datos = lee_datos_extranjeria(ruta_fichero)
    print(f"Se han leido {len(datos)} entradas de datos")
    print(f"Las tres primeras son {datos[:3]}")
    print()

if __name__ == '__main__':
    test_lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    datos = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    