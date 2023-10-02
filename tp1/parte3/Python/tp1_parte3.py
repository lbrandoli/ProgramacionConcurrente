import os
import multiprocessing

# Función que realiza el cálculo de estadísticas
def calculate_statistics(words):
    """
    Calcula estadísticas sobre una lista de palabras.

    :param words: Una lista de palabras para analizar.
    :type words: list
    :return: Una tupla con las estadísticas calculadas: 
             (total_caracteres, total_letras, total_digitos, palabra_mas_larga, palabra_mas_corta)
    :rtype: tuple
    """
    if not words:
        return 0, 0, 0, '', ''

    total_characters = sum(len(word) for word in words)
    total_letters = sum(c.isalpha() for word in words for c in word)
    total_digits = sum(c.isdigit() for word in words for c in word)
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    return total_characters, total_letters, total_digits, longest_word, shortest_word


# Función del proceso hijo
def child_process(pipe):
    """
    Función que se ejecuta en el proceso hijo.

    :param pipe: La tubería de comunicación con el proceso padre.
    :type pipe: multiprocessing.Pipe
    """
    words = []
    while True:
        word = pipe.recv()
        if word == "close":
            break
        words.append(word)

    statistics = calculate_statistics(words)
    pipe.send(statistics)
    pipe.close()


if __name__ == "__main__":
    parent_pipe, child_pipe = multiprocessing.Pipe()

    child_process = multiprocessing.Process(target = child_process, args=(child_pipe,))
    child_process.start()

    words = []
    while True:
        word = input("Ingrese una palabra (o 'close' para finalizar): ")
        if word == "close":
            break
        parent_pipe.send(word)

    parent_pipe.send("close")
    child_process.join()

    statistics = parent_pipe.recv()
    parent_pipe.close()

    total_characters, total_letters, total_digits, longest_word, shortest_word = statistics

    print(f"Total de caracteres: {total_characters}")
    print(f"Total de letras: {total_letters}")
    print(f"Total de dígitos: {total_digits}")
    print(f"Palabra más larga: {longest_word}")
    print(f"Palabra más corta: {shortest_word}")

