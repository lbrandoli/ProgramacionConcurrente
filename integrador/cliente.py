import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

from crypto import cifrar_mensaje, descifrar_mensaje

clave = False
clave_general = ""


class Cliente:
    def __init__(self, ventana):
        """
        Inicializa la interfaz gráfica del cliente y establece la conexión con el servidor.

        :param ventana: Objeto de la ventana de la aplicación Tkinter.
        """
        self.ventana = ventana
        self.ventana.title("Cliente de Mensajes")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

        self.text_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.entry = tk.Entry(ventana, width=30)
        self.entry.grid(row=1, column=0, padx=10, pady=10)

        self.boton_enviar = tk.Button(ventana, text="Enviar Mensaje", command=self.enviar_mensaje)
        self.boton_enviar.grid(row=1, column=1, padx=10, pady=10)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectar()

        # Inicia un hilo para recibir mensajes
        self.hilo_receptor = threading.Thread(target=self.recibir_mensajes)
        self.hilo_receptor.start()

    def conectar(self):
        """
        Establece la conexión con el servidor.

        :return: None
        """
        HOST = '127.0.0.1'
        PORT = 5555
        self.sock.connect((HOST, PORT))

    def enviar_mensaje(self):
        """
        Envia un mensaje al servidor.

        :return: None
        """
        mensaje = self.entry.get()
        # Cifrado del mensaje
        mensaje = cifrar_mensaje(mensaje, clave_general)
        # self.sock.send(mensaje.encode())
        self.sock.send(mensaje)
        if mensaje.lower() == "salir":
            self.sock.close()
            self.ventana.destroy()

        # Limpiar la caja de texto después de enviar el mensaje
        self.entry.delete(0, tk.END)

    def recibir_mensajes(self):
        """
        Recibe mensajes del servidor y los muestra en la interfaz gráfica.

        :return: None
        """
        while True:
            try:
                mensaje = self.sock.recv(1024).decode()
                global clave
                global clave_general
                if not clave:
                    clave = True
                    clave_general = mensaje
                if ":" in mensaje:
                    cabecera = mensaje.split(":")[0]
                    mensaje_cifrado = mensaje.split(":")[1].strip()
                    mensaje_cifrado = mensaje_cifrado.encode('latin-1')

                    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave_general)
                    self.text_area.insert(tk.END, f"{cabecera}{mensaje_descifrado}\n")
                    self.text_area.yview(tk.END)
                else:
                    self.text_area.insert(tk.END, f"{mensaje}\n")
                    self.text_area.yview(tk.END)
            except:
                break

    def cerrar_aplicacion(self):
        """
        Cierra la aplicación y envía un mensaje al servidor indicando que el cliente está cerrando.

        :return: None
        """
        self.sock.send("salir".encode())
        self.sock.close()
        self.ventana.destroy()


# Inicia la interfaz gráfica del cliente
root = tk.Tk()
cliente = Cliente(root)
root.mainloop()
