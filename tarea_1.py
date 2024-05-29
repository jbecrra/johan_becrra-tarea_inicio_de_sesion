import os
import time
import msvcrt

print("1. Inicio de sesión")
print("2. Registrar usuario")
print("3. Eleiminar usuario")
print("4. Salir")
while True:
    opc=int(input("ingrese opcion: "))
    if opc==1:
        pass
    elif opc==2:
        print("REGISTRO DE USUARIO")
        nombre=input("ingrese nombre: ")
        password=input("ingrese contraseña: ")
        usuario={
            "nombre": nombre,
            "password": password
        }
        print("usuario agregado con éxito!")
    elif opc==3:
        pass
    else:
        print("ADIOS!")