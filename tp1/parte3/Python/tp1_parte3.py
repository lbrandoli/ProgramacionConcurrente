import os
import multiprocessing

# Función para calcular estadísticas
def calcular_estadisticas(palabras):
    total_caracteres = 0
    total_letras = 0
    total_digitos = 0
    palabra_mas_larga = ""
    palabra_mas_corta = ""

    if not palabras:
        return total_caracteres, total_letras, total_digitos, palabra_mas_larga, palabra_mas_corta

    for palabra in palabras:
        total_caracteres += len(palabra)
        total_letras += sum(c.isalpha() for c in palabra)
        total_digitos += sum(c.isdigit() for c in palabra)

        if not palabra_mas_larga or len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

        if not palabra_mas_corta or len(palabra) < len(palabra_mas_corta):
            palabra_mas_corta = palabra

    return total_caracteres, total_letras, total_digitos, palabra_mas_larga, palabra_mas_corta


# Función del proceso hijo
def proceso_hijo(pipe):
    palabras = []

    while True:
        word = pipe.recv()
        if word == "close":
            break
        palabras.append(word)
    stats = calcular_estadisticas(palabras)
    pipe.send(stats)
    pipe.close()


def run():
    padre_pipe, hijo_pipe = multiprocessing.Pipe()

    proceso = multiprocessing.Process(target=proceso_hijo, args=(hijo_pipe,))
    proceso.start()

    palabras = []
    while True:
        palabra = input("Ingrese una palabra (o 'close' para finalizar): ")
        if palabra == "close":
            break
        padre_pipe.send(palabra)

    padre_pipe.send("close")
    proceso.join()

    estadisticas = padre_pipe.recv()
    padre_pipe.close()

    total_caracteres, total_letras, total_digitos, palabra_mas_larga, palabra_mas_corta = estadisticas

    print(f"Total de caracteres: {total_caracteres}")
    print(f"Total de letras: {total_letras}")
    print(f"Total de dígitos: {total_digitos}")
    print(f"Palabra más larga: {palabra_mas_larga}")
    print(f"Palabra más corta: {palabra_mas_corta}")


if __name__ == "__main__":
  run()