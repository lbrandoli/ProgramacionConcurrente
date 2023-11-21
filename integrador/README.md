# ProgramacionConcurrente
# Integrador - Sistema

### Integrantes:
       
    Brandoli Lucio          42115988    lbrandoli@alumno.unlam.edu.ar
    Camejo Luciano          41764906    lcamejo@alumno.unlam.edu.ar 
    Meza Julian             39463982    jmeza@alumno.unlam.edu.ar 
    Miranda Segio Javier    35634266    semiranda@alumno.unlam.edu.ar 


# Sistema de Mensajería Cliente-Servidor con Tkinter y Encriptación

Este proyecto implementa un sistema de mensajería cliente-servidor en Python utilizando la biblioteca `tkinter` para la interfaz gráfica y `socket` para la comunicación entre el cliente y el servidor. Además, se incorpora un sistema de encriptación de mensajes mediante la biblioteca `cryptography`.

## Contenido del Proyecto

- `main.py`: Inicia un servidor como proceso principal y dos clientes como procesos secundarios, permitiendo la comunicación entre ellos en un sistema de mensajería cliente-servidor
- `server.py`: El código del servidor que acepta conexiones de clientes, maneja múltiples conexiones y decodifica los mensajes encriptados.
- `client.py`: El código del cliente que se conecta al servidor, envía mensajes encriptados y proporciona una interfaz gráfica para interactuar con el usuario.

## Requisitos

- Python 3.x
- `cryptography` (puedes instalarlo con `pip install cryptography`)

## Instrucciones de Uso

1. Ejecuta `server.py` para iniciar el servidor.
2. Ejecuta `client.py` para iniciar un cliente. Puedes ejecutar múltiples clientes para simular una conversación.
3. Ingresa mensajes en la interfaz gráfica del cliente y presiona "Enviar Mensaje".
4. Los mensajes encriptados se enviarán al servidor y se mostrarán en la consola del servidor.

* Puede ejecutar `main.py` para automatiocar su ejecucion, el cual Iniciar el servidor como un proceso padre y dos clientes como procesos hijos

## Características

- Mensajería Cliente-Servidor
- Interfaz Gráfica con Tkinter
- Encriptación de Mensajes con `cryptography`
- Manejo de Conexiones Múltiples mediante Hilos

### Notas


