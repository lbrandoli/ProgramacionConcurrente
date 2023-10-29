from mpi4py import MPI
import numpy as np
from IPython.display import display
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

count = 5000
sendbuf = None

def main():
    if rank == 0:
        sendbuf = np.random.randn(size, count)
        display("Máximo de matriz calculado con metodo: ", sendbuf.max())
        initWork(comm, sendbuf, size) #En esta funcion trabaja el proceso raiz
    else:
        doWork(comm)    #Aqui trabajan todos los procesos distintos al proceso raiz

def initWork(comm, matrix, cantProcess):
    rowCount = 1    #Los procesos que lanzaremos empezaran a calcular el maximo desde la fila 1 y no desde la fila 0
    recvCount = 1   #La cantidad de procesos que esperamos tambien empieza en 1 ya que el proceso 0 no se espera
    maxArray = []   #Aqui se almacenaran los valores maximos de cada fila
    
    maxArray.append(max(matrix[0])) #El proceso 0 calcula el valor maximo de la fila 0

    #En este for vamos lanzando los procesos y les asignamos cual es la fila en la que tienen que encontrar el maximo
    #Empieza en el proceso 1 ya que el proceso 0 es el raiz
    for id in range(1, cantProcess):
        if rowCount < len(matrix):
            comm.send(matrix[rowCount], dest = id) #Al proceso con id <id> se le asigna la fila <rowCount> para buscar su maximo
            rowCount += 1
    
    #En este while vamos a esperar a que todos los procesos devuelvan el valor maximo que calcularon de cada fila
    while recvCount < cantProcess:
        stat = MPI.Status()
        maxOfRow = comm.recv(source=MPI.ANY_SOURCE, status=stat)    #En esta variable vamos a almacenar el valor que devuelve cada proceso al calcular el maximo de cada fila
        maxArray.append(maxOfRow)
        recvCount += 1
        
    print("Maximo de matriz calculado con MPI: ", max(maxArray))
        
def doWork(comm):
    stat = MPI.Status()
    row = comm.recv(source=0, status=stat) #Aqui recibimos la informacion que nos manda el proceso raiz
    comm.send(max(row), dest = 0)   #Aqui enviamos al proceso raiz el valor maximo calculado en la fila

main()