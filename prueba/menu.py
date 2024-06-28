import prueba


def menu2():
    print(""" 
Para comprar cada item tiene que ingresar todos sus datos 
|----------------------------|-------------------
1) | Abono | 
2) | Tierra |
3) | Lirio |
4) | Rosas Rojas 
5) | Margaritas """)




def menu():
    print(""" 
Para comprar cada item tiene que ingresar todos sus datos 
|----------------------------|-------------------
1) | Abono | 
2) | Tierra |
3) | Lirio |
4) | Rosas Rojas 
5) | Margaritas
7) listar """)
    while True:
        opcion = int(input("ingrse una opcion "))
        if opcion == 1:
            prueba.agregar()
        elif opcion ==2:
            prueba.agregar()
        elif opcion == 3:
            prueba.agregar()
        elif opcion == 4:
            prueba.agregar()
        elif opcion == 5:
            prueba.agregar()
        elif  opcion == 6:
            prueba.listar()
        elif opcion == 7:
            break
        else:
            print("Ingrese una opcion valida")

menu()