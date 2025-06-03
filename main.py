import pandas as pd

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            calificaciones = list(map(float, input("Ingresa las calificaciones separadas por comas: ").split(",")))
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Error: Ingresa solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        promedios[nombre] = promedio
    return promedios

def obtener_mejor_estudiante(promedios):
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_resultados(estudiantes, promedios, mejor_estudiante):
    with open("resultados.txt", "w") as archivo:
        for nombre, notas in estudiantes.items():
            archivo.write(f"{nombre}: {notas} - Promedio: {promedios[nombre]:.2f}\n")
        archivo.write(f"\nMejor estudiante: {mejor_estudiante[0]} con promedio de {mejor_estudiante[1]:.2f}\n")

def main():
    estudiantes = ingresar_datos()
    if not estudiantes:
        print("No se ingresaron datos.")
        return
    promedios = calcular_promedios(estudiantes)
    mejor_estudiante = obtener_mejor_estudiante(promedios)
    guardar_resultados(estudiantes, promedios, mejor_estudiante)
    print("Resultados guardados en 'resultados.txt'.")

if __name__ == "__main__":
    main()
