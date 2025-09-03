import json

"""
with open("prueba.txt", "r") as f:
    godrick = f.read()
    print(godrick)
    pos = f.tell()
    print(pos)
    print("El archivo tiene {0} caracteres".format(len(godrick)))
    print(f.closed)
    
with open("prueba2.txt", "w") as f1:    
    f1.write("Your skin.. oh yeah your skin and bones.." \
    "\n turn into something beautiful\n you know, you know I love you so")
    print("Archivo creado")

with open("prueba2.txt", "a") as f2:
    f2.write("\n look at the stars, look how they shine for you")
    print("Archivo modificado")

with open("prueba2.txt", "r") as f3:
    contenido = f3.read()
    print(contenido)
    print("El archivo tiene {0} caracteres".format(len(contenido)))


with open("prueba3.txt", "w") as f4:
    f4.write("\n \n i walked across an empty land\n i knew the pathway like the back of my hand\n"
    " i felt the earth beneath my feet\n sat by the river and it made me complete"
    "\n oh simply thing where have you gone\n i'm getting old and i need something to rely on"
    "\n so tell me when you're gonna let me in\n i'm getting tired and i need somewhere to begin"
    "   \n i came across a fallen tree\n i felt the branches of it looking at me" 
    "\n is this the place we used to love\n is this the place that I've been dreaming of"
    "\n oh simple thing where have you gone\n i'm getting old and i need something to rely on"
    "\n so tell me when you're gonna let me in\n i'm getting tired and i need somewhere to begin"
    "\n and if you have a minute why don't we go\n talk about it somewhere only we know"
    "\n this could be the end of everything\n so why don't we go somewhere only we know"
    "\n somewhere only we know")   
    print("Archivo creado")




json_str='{"nombre": "John", "edad": 30, "pais": "USA"}'
print(json_str)
print(type(json_str))

python_dict = json.loads(json_str)
print(python_dict)
print(type(python_dict))
print(python_dict['edad'])
print(python_dict['pais'])




data = {
    "nombre": "Keinerth",
    "edad": 19,
    "pais": "Colombia",
    "Juegos": ["Dark Souls", "Dark souls II", "Dark Souls III", "Elden Ring", "Sekiro"]
}
json_data = json.dumps(data)
print(json_data)
print(type(json_data))

"""


"""
data = {
    "nombre": "Keinerth",
    "edad": 19,
    "pais": "Colombia",
    "Juegos": ["Dark Souls", "Dark souls II", "Dark Souls III", "Elden Ring", "Sekiro"]
}
#json_data = json.dumps(data, indent=4, separators=(", ", " : "))
json_data = json.dumps(data, indent=4, separators=(", ", " : "), sort_keys=True)
print(json_data)
"""
"""
json_data = json.JSONEncoder().encode({"lenguajes": ["Python", "JavaScript"]})
print(json_data)
print(type(json_data))
"""
"""
class Curso():
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
curso_1 = Curso("2468", "Estructura de datos", 3)
print(curso_1)


json_object_data = json.dumps(curso_1.__dict__)
print(json_object_data)
print(type(json_object_data))


python_dict= json.loads(json_object_data)
print(python_dict)
print(type(python_dict))
"""

















