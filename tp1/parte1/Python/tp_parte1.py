import os
import time

PROCESO_A = "A"
PROCESO_B = "B"
PROCESO_C = "C"
PROCESO_D = "D"
PROCESO_E = "E"
PROCESO_F = "F"
PROCESO_G = "G"
PROCESO_H = "H"
TIME_SLEEP = 200
PID_NULL = 0

def processMessage(node):
    message = "soy el proceso {name}. PID: {pid}. PPID {ppid}\n"
    print(message.format(name=node,pid=os.getpid(),ppid=os.getppid()))

def spawnProcesses(node):
    pid=PID_NULL
    name,children = node
    processMessage(name)
    for item in children:
        pid=os.fork()
        if pid < PID_NULL:
            print("Error al crear nuevo proceso")
            os._exit(1)
        if not pid:
            spawnProcesses(item)
            time.sleep(TIME_SLEEP)
            os._exit(0)
    for item in children:
        os.wait()

def main():
    tree = (PROCESO_A, [(PROCESO_B,[(PROCESO_D,[]), (PROCESO_E,[(PROCESO_G,[]), (PROCESO_H,[])])]),(PROCESO_C,[(PROCESO_F,[])])])
    spawnProcesses(tree)
    os._exit(0)

if __name__ == "__main__":
    main()