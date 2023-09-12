import time
import threading
import random


def suma_secuencial(M1, M2, N):
    RS = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            RS[i][j] = M1[i][j] + M2[i][j]
    return RS

def suma_concurrente(M1, M2, N):
    hilos = []
    RC = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        hilo = threading.Thread(target=suma_fila, args=(i, M1, M2, RC, N,))
        hilos.append(hilo)
        hilo.start()
    for hilo in hilos:
        hilo.join()
    return RC

def suma_fila(i, M1, M2, RC, N):
    for j in range(N):
        RC[i][j] = M1[i][j] + M2[i][j]
        
def comparar_matrices(M1, M2, N):
    for i in range(N):
        for j in range(N):
            if (M1[i][j] != M2[i][j]):
                return False
    return True


def main():
    N = 5
    A = [[random.randint(-32, 32) for _ in range(N)] for _ in range(N)]
    B = [[random.randint(-32, 32) for _ in range(N)] for _ in range(N)]
    
    CS = suma_secuencial(A, B, N)
    CC = suma_concurrente(A, B, N)

    print("Matriz A:\n", A)
    print("Matriz B:\n", B)
    print("Matriz resultado de la suma secuencial:\n", CS)
    print("Matriz resultado de la suma concurrente:\n", CC)

    if (comparar_matrices(CS, CC, N)):
        print("\nAl comparar las matrices se determinó que son iguales")
    else:
        print("\nAl comparar las matrices se determinó que son diferentes")


if __name__ == "__main__":
    main()