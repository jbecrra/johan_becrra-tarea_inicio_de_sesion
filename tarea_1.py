import os
import time
usuarios=[] 
while True:
    os.system('cls')
    print("1. Inicio de sesión")
    print("2. Registrar usuario")
    print("3. Eleiminar usuario")
    print("4. Salir")
    while True:
        try:
            opc=int(input("ingrese opcion: "))
            if opc in(1,2,3,4,):
                break
            else:
                print("ERROR! debe ingresar una opcion del menú")
        except:
            print("ERROR! debe ingresar un numero entero")
    if opc==1:
        os.system('cls')
        print("INICIO DE SESION")
        nombre=input("ingrese nombre: ")
        password=input("ingrese contraseña: ")
        for x in range(len(usuarios)):
            if usuarios[x]["nombre"]==nombre:
                if usuarios[x]["password"]==password:
                    print("inicio de sesion exitoso!")
            else:
                print("usuario o contraseña erronea!")
        time.sleep(3)
    elif opc==2:
        os.system('cls')
        print("REGISTRO DE USUARIO")
        nombre=input("ingrese nombre: ")
        password=input("ingrese contraseña: ")
        usuario={
            "nombre": nombre,
            "password": password
        }
        usuarios.append(usuario)
        print("USUARIO AGREGADO!")
        time.sleep(3)
    elif opc==3:
        os.system('cls')
        print("ELIMINAR USUARIO!")
        nombre=input("ingrese el nombre: ")
        for x in range(len(usuarios)):
            if usuarios[x]["nombre"]==nombre:
                usuarios.pop(x)
                break
        print("USUARIO ELIMINADO!")
        time.sleep(3)
    else:
        print("ADIOS!")
        break