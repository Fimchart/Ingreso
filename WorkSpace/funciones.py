def guardar_usuarios(nombre, contraseña):
    with open ("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre}:{contraseña}\n")


def cargar_usuarios():
    usuarios = {}
    try:
        with open ("usuarios.txt", "r") as archivo:
            for linea in archivo:
                if ":" in linea:
                    nombre, contraseña = linea.strip().split(":")
                    usuarios [nombre] = contraseña
    except FileNotFoundError:
        pass
    return usuarios

def iniciar_sesion(usuarios):
    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return False
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"\nBienvenido {usuario}")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False


def registro_contraseña():
    while True:
        contraseña = input("Ingrese la contraseña: ")
        confirmar = input("Ingrese la contraseña nuevamente: ")
        if contraseña == confirmar:
            return contraseña
        else: 
            print("Las contraseñas no coinciden.")
            print("Vuelva a intentarlo.")

def menu():
    print("\n1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir\n")


def menuuu():
    print("\n1. Realizar llamada")
    print("2. Enviar correo electronico")
    print("3. Cerrar sesión\n")


def numero():
    while True:
        numero = input("Ingrese el numero a llamar: ")
        if numero.isdigit() and len(numero) == 9 and numero.startswith("9"):
            print("---- LLAMANDO ----")
            return
        else:
            print("El numero no es valido.")
            print("Intentelo de nuevo.")


def solicitar_correo():
    while True:
        correo = input("Ingrese el correo electronico: ")

        tiene_arroba = False
        tiene_punto = False
        for caracter in correo:
            if caracter == "@":
                tiene_arroba = True
                continue
            elif caracter == ".":
                tiene_punto = True
        if tiene_arroba and tiene_punto:
            print(f"El correo: {correo} fue ingresado.")
            return correo
        else:
            print("\nCorreo invalido.")
            print("Intentelo de nuevo.\n")


def usuario_activo():
    while True:
        menuuu()
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Solo se pueden ingresar numeros.")
            continue

        if opcion == 1:
            numero()
        elif opcion == 2:
            solicitar_correo()
            input("Escriba el mensaje: \n")
        elif opcion == 3:
            print("----- CERRANDO SESIÓN -----")
            break
        else:
            print("Opcion no valida.")

