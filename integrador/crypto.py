from cryptography.fernet import Fernet

def gen_clave():
    """
    Genera una clave para cifrar y descifrar mensajes usando Fernet.

    :return: Clave generada.
    """
    clave = Fernet.generate_key()
    return clave

def cifrar_mensaje(mensaje, key):
    """
    Cifra un mensaje utilizando una clave proporcionada.

    :param mensaje: Mensaje a cifrar.
    :param key: Clave utilizada para cifrar el mensaje.
    :return: Mensaje cifrado.
    """
    cipher_suite = Fernet(key)
    mensaje_bytes = mensaje.encode()
    mensaje_cifrado = cipher_suite.encrypt(mensaje_bytes)
    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado,key):
    """
    Descifra un mensaje cifrado utilizando una clave proporcionada.

    :param mensaje_cifrado: Mensaje cifrado a descifrar.
    :param key: Clave utilizada para descifrar el mensaje.
    :return: Mensaje descifrado.
    """
    cipher_suite = Fernet(key)
    mensaje_bytes = cipher_suite.decrypt(mensaje_cifrado)
    return mensaje_bytes.decode()

