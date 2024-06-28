import json



def agregar():
    with open("greengarden.json",mode="r") as r:
        lectura = json.load(r)
    while True:

        nom = input("ingrese su nombre ")
        dic = input("ingrese su direccion ")
        num = input("ingrese su numero de telefono ")
        ped = input("ingrese el tipo de pedido ")
        can = int(input("ingrese la cantidad"))
        break


    lista ={   
            "id":len(lectura["reguistro"])+1,
            "nombre": nom,
            "direccion": dic,
            "numero": num,
            "pedido": ped,
            "cantidad": can
        }

    
    lectura["reguistro"].append(lista)

    with open("greengarden.json",mode="w") as w:
        json.dump(lectura,w,indent=4)

def listar():
    with open("greengarden.json",mode="r") as r:
        lectura = json.load(r)

        for i in lectura["reguistro"]:
            print(i,end="\n",sep="   ")




def recibo():
    with open("greengarden.json",mode="r") as r:
        lectura = json.load(r)


        
        
        
        

    nombre = lectura["reguistro"][0]["nombre"] 

    print(f"""
    BOLETA

NOMBRE:{nombre}
DIRECCION:
NUNERO:
PEDIDO:
CANTIDAD:
              """)
        
