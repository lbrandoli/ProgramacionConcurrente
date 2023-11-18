import socket
import threading

from crypto import gen_clave

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 5555

# Diccionario para almacenar clientes conectados y sus direcciones
clientes = {}


# Función para manejar la conexión de un cliente
def manejar_cliente(cliente, direccion):
    """
    Maneja la conexión de un cliente.

    :param cliente: Objeto de socket representando al cliente.
    :param direccion: Tupla que contiene la dirección IP y el puerto del cliente.
    """
    print(f"[Nueva conexión] {direccion} conectado.")

    # Compartir clave genera del servidor al cliente
    cliente.send(clave_genera)
    # Envía un mensaje de bienvenida al cliente
    cliente.send("Bienvenido al servidor de mensajes".encode())

    while True:
        try:
            mensaje = cliente.recv(1024).decode()
            if mensaje.lower() == "salir":
                break

            # Envia el mensaje a todos los clientes
            enviar_a_todos(f"{direccion}: {mensaje}", cliente)
        except:
            break

    print(f"[Desconexión] {direccion} desconectado.")
    eliminar_cliente(cliente)


# Función para enviar un mensaje a todos los clientes, excepto al remitente
def enviar_a_todos(mensaje, remitente):
    """
    Envía un mensaje a todos los clientes, excepto al remitente.

    :param mensaje: Mensaje a enviar.
    :param remitente: Cliente que envió el mensaje, para evitar enviar el mensaje de vuelta a este cliente.
    """
    for cliente, direccion in clientes.items():
        if cliente != remitente:
            try:
                cliente.send(mensaje.encode())
            except:
                eliminar_cliente(cliente)


# Función para eliminar a un cliente de la lista
def eliminar_cliente(cliente):
    """
    Elimina a un cliente de la lista de clientes conectados.

    :param cliente: Objeto de socket representando al cliente a ser eliminado.
    """
    direccion = clientes[cliente]
    del clientes[cliente]
    cliente.close()
    enviar_a_todos(f"{direccion} se ha desconectado.", None)


# Configuración del socket del servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor escuchando en {HOST}:{PORT}")
clave_genera = gen_clave()

while True:
    cliente, direccion = servidor.accept()
    clientes[cliente] = direccion

    # Inicia un hilo para manejar al cliente
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
    hilo_cliente.start()
