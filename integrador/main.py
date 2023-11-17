import subprocess
import time

def iniciar_servidor():
    """
    Inicia el servidor.
    """
    subprocess.run(["python", "servidor.py"])

def iniciar_cliente():
    """
    Inicia un cliente.
    """
    subprocess.run(["python", "cliente.py"])

if __name__ == "__main__":
    # Iniciar el servidor como un proceso padre
    servidor_proceso = subprocess.Popen(["python", "servidor.py"])

    # Esperar un breve momento antes de iniciar los clientes
    time.sleep(2)

    # Iniciar dos clientes como procesos hijos
    cliente_proceso_1 = subprocess.Popen(["python", "cliente.py"])
    cliente_proceso_2 = subprocess.Popen(["python", "cliente.py"])

    # Esperar a que los procesos hijos terminen
    cliente_proceso_1.wait()
    cliente_proceso_2.wait()

    # Terminar el servidor después de que los clientes hayan terminado
    servidor_proceso.terminate()
