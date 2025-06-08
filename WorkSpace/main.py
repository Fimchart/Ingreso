from funciones import guardar_usuarios, cargar_usuarios, registro_contraseña, iniciar_sesion
from funciones import menu, menuuu, numero, solicitar_correo, usuario_activo

usuarios = cargar_usuarios()

print("\n----- Bienvenid@ -----")
while True:
    menu()
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Solo se pueden ingresar numeros.")
        continue

    if opcion == 1:
        if iniciar_sesion(usuarios):
            usuario_activo()
    elif opcion == 2:
        if len(usuarios) >= 3:
            print("\n Ya se han registrsdo la capacidad maxima de usuarios.")
            continue

        nuevo_usuario = input("Ingrese el nombre de usuario: ")
        if nuevo_usuario in usuarios:
            print("Ese nombre de usuario ya esta ocupado.")
            continue

        nueva_contraseña = registro_contraseña()
        usuarios[nuevo_usuario] = nueva_contraseña
        guardar_usuarios(nuevo_usuario, nueva_contraseña)
        print(f"¡El usuario {nuevo_usuario} ha sido registrado con exito!")
    elif opcion == 3:
        print("----- SALIENDO -----")
        break
    else:
        print("Opcion no valida.")
        break