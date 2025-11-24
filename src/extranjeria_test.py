from extranjeria import *

def test_lee_datos_extranjeria(ruta_fichero: str) -> None:
    print("Probando lee_datos_extranjeria()...")

    datos = lee_datos_extranjeria(ruta_fichero)
    print(f"Se han leido {len(datos)} entradas de datos")
    print(f"Las tres primeras son {datos[:3]}")
    print()


def test_numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> None: 
    print("Probando numero_nacionalidades_distintas()...")

    nacionalidades = numero_nacionalidades_distintas(registros)
    print(f"El numero de nacionalidades distintas es {nacionalidades}")
    print()


def test_secciones_distritos_con_extranjeros_nacionalidades(registros: list[RegistroExtranjeria], paises: set[str]) -> None:

    print("Probando secciones_distritos_con_extranjeros_nacionalidades()") 

    secciones_distritos = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(f"Las secciones por distritos son {secciones_distritos}")
    print()


def test_total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> None: 
    print("Probando total_extranjeros_por_pais()...")

    extranjeros_pais = total_extranjeros_por_pais(registros)
    print(f"Los datos del total de extranjeros por paises son {list(extranjeros_pais.items())}")
    print()


def test_top_n_extranjeria(registros: list[RegistroExtranjeria], n: int = 3) -> None:
    print("Probando top_n_extranjeria()...")

    paises = top_n_extranjeria(registros, n)
    print(f"Los paises con más población extranjera son {paises}")
    print()


def test_barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> None: 
    print("Probando barrio_mas_multicultural()...")

    barrio_max = barrio_mas_multicultural(registros)
    print(f"El barrio con más países es {barrio_max}")
    print()


def test_barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo: str = None) -> None: 
    print("Probando barrio_con_mas_extranjeros()...")

    barrio_max = barrio_con_mas_extranjeros(registros, tipo)
    print(f"El barrio con más {tipo} es {barrio_max}")
    print()


def test_pais_mas_representado_por_distrito(registros: list[RegistroExtranjeria]) -> None: 
    print("Probando pais_mas_representado_por_distrito()...")

    pais_distrito = pais_mas_representado_por_distrito(registros)
    print(f"El pais más representado por distrito es {pais_distrito}")
    print()


if __name__ == '__main__':
    test_lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    registros = lee_datos_extranjeria("data/extranjeriaSevilla.csv")

    test_numero_nacionalidades_distintas(registros)

    test_secciones_distritos_con_extranjeros_nacionalidades(registros, {'ITALIA', 'ALEMANIA'})

    test_total_extranjeros_por_pais(registros)

    test_top_n_extranjeria(registros)
    test_top_n_extranjeria(registros, 5)

    test_barrio_mas_multicultural(registros)

    test_barrio_con_mas_extranjeros(registros)
    test_barrio_con_mas_extranjeros(registros, 'Hombres')
    test_barrio_con_mas_extranjeros(registros, 'Mujeres')

    test_pais_mas_representado_por_distrito(registros)