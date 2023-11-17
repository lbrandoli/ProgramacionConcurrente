import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class Cliente:
    def __init__(self, ventana):
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
        HOST = '127.0.0.1'
        PORT = 5555
        self.sock.connect((HOST, PORT))

    def enviar_mensaje(self):
        mensaje = self.entry.get()
        self.sock.send(mensaje.encode())
        if mensaje.lower() == "salir":
            self.sock.close()
            self.ventana.destroy()

        # Limpiar la caja de texto después de enviar el mensaje
        self.entry.delete(0, tk.END)

    def recibir_mensajes(self):
        while True:
            try:
                mensaje = self.sock.recv(1024).decode()
                self.text_area.insert(tk.END, f"{mensaje}\n")
                self.text_area.yview(tk.END)
            except:
                break

    def cerrar_aplicacion(self):
        self.sock.send("salir".encode())
        self.sock.close()
        self.ventana.destroy()

# Inicia la interfaz gráfica del cliente
root = tk.Tk()
cliente = Cliente(root)
root.mainloop()
