"""
Proceso supuesto:

gramos consumidos -> calorias consumidas
                  -> Cantidad de comida semanal necesaria por ingrediente

Algoritmo:
1. Obtener los gramos consumidos de cada ingrediente
2. Calcular las calorias consumidas
    a. Transformar los gramos consumidos a calorias
    b. Sumar las calorias de cada ingrediente
    c. Mostrar las calorias consumidas
3. Calcular la cantidad de comida semanal necesaria por ingrediente
4. Mostrar los resultados
"""


gramos_consumidas = {
    "pan" : 66,
    "leche" : 200,
    "huevo" : 150,
    "pasta" : 200,
    "carne" : 150,
    "carne" : 200,
    "arroz" : 200,
    "platano" : 300,
}



api_calorias_100g = {
    "huevo": 155,
    "pan": 265,
    "leche": 60,
    "avena": 389,
    "yogur": 59,
    "manzana": 52,
    "platano": 96,
    "naranja": 43,
    "pollo": 165,
    "carne": 250,
    "pescado": 206,
    "arroz": 130,
    "pasta": 131,
    "patata": 77,
    "zanahoria": 41,
    "brocoli": 55,
    "espinaca": 23,
    "tomate": 18,
    "cebolla": 40,
    "aceite": 884,
    "mantequilla": 717,
    "azucar": 387,
    "sal": 0,
    "pimienta": 251,
    "limon": 29,
    "nuez": 654,
    "almendra": 579,
    "avellana": 628,
    "cacahuete": 567,
    "chocolate": 546,
    "galleta": 502,
    "helado": 207,
    "refresco": 41,
    "agua": 0
}

gramos_semanales = {}
# a partir de aquí empieza el programa
calorias_consumidas_dia_por_ingrediente = {}
calorias_consumidas_dia = 0

# 1. Obtener los gramos consumidos de cada ingrediente, 2. Calcular las calorias consumidas totales y 3. Calcular la cantidad de comida semanal necesaria por ingrediente
for ingrediente, gramos in gramos_consumidas.items():
    gramos_semanales[ingrediente] = gramos * 7
    calorias_100g = api_calorias_100g[ingrediente]
    calorias = (gramos * calorias_100g) / 100
    calorias_consumidas_dia += calorias
    calorias_consumidas_dia_por_ingrediente[ingrediente] = calorias

# Ver los resultados
print("Calorias consumidas al día: ", calorias_consumidas_dia)
print("Gramos semanales necesarios por ingrediente: ", gramos_semanales)
print("Calorias consumidas al día por ingrediente: ", calorias_consumidas_dia_por_ingrediente)