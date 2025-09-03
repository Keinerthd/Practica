import csv


"""
try: 
    with open("text.txt", "r+") as f:
        cont = f.read()
        print("Contenido del archivo")
        print(cont)
        f.seek(0)
        f.write("Nuevo contenido.\n" + cont)
except Exception as e:
    print("Ha ocurrido un error: ", e)        
"""

"""
with open("test.csv", "r") as f:
    lector = csv.reader(f)
    for row in lector:
        print("Ap paterno: {0}, Ap materno: {1}, Nombre: {2}, Ciudad: {3}".format(row[0], row[1], row[2], row[3]))
"""
"""
with open("test.csv", "r") as f:
    lector = csv.reader(f)
    with open("test_writer.csv", "w", newline= "") as f2:
        escritor = csv.writer(f2, delimiter = "|")
        for row in lector:
            escritor.writerow(row)
"""
"""
devices = [
    ['hostname','ip','username','password'],
    ['R1','G0/0','10.10.10.1','1234'],
    ['R2','G0/0','10.20.20.1','hola23']
]


with open("devices.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerows(devices)
"""
"""
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', '19', 'Barcelona'],
    ['Esteban', '22', 'Cadiz'],
    ['Julio', '38', 'roma']
]

nombre = "datos.csv"
with open(nombre, "w", newline="") as f:
    escritor = csv.writer(f)
    for fila in datos:
        escritor.writerow(fila)
    
print(f"Archivo {nombre} creado con exito")
"""



#Crea un programa que permita a un usuario registrar informacion y almacenarla en un archivo de
#csv. 

"""
def registrar():
    print("\n --- REGISTRANDO USUARIO ---")
    nombre = input("Ingrese su usuario:")
    edad = input("Ingrese su edad:")
    ciudad = input("Ingrese su ciudad:")
    
    archivo = "usuarios.csv"
    try:
        with open(archivo, "r") as f:
            pass
        encabezado = False
    except FileNotFoundError:
        encabezado = True
        

    with open(archivo, "a", newline="") as f:
        escritor = csv.writer(f)
        if encabezado:
            escritor.writerow(["Nombre", "Edad", "Ciudad"])
        escritor.writerow([nombre, edad, ciudad])
        print("Usuario registrado con exito")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Registrar usuario")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")
    
        if opcion == "1":
            registrar()
        elif opcion == "2":
            print("Saliendo del sistema...*")
            break
        else:
            print ("opcion no valida")


menu()              
"""
#Crea un programa que permita a un usuario registrar informacion (nombre, correo, numero)
# y almacenar la informacion en una matriz y lo colocas en un archivo de csv. 
"""
usuarios = [
    ["Nombre", "Correo", "Numero"]

]


def menu():
    while True:
        print("\n --- MENU ---")
        print("1. Registrar usuario")
        print("2. Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            print("Saliendo del sistema...*")
            break
        else:
            print("Opcion no valida")

def registrar():
    print("\n --- REGISTRANDO USUARIO ---")
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    numero = input("Ingrese su numero: ")

    archivo = "usuarios2.csv"
    with open(archivo, "a", newline="") as f:
        escritor = csv.writer(f)
        if len(usuarios) == 1:
            escritor.writerow(usuarios[0])
        usuarios.append([nombre, correo, numero])
        escritor.writerow([nombre, correo, numero])
        print("Usuario registrado con exito")
            
   

menu()
"""



with open("ejemplo.csv", "r") as f:
    lector = csv.readline(f)

for i in range(10):
    with open("ejemplo.csv", "r") as f:
    













