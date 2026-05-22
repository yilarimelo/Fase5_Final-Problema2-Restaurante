# Estudiantes-Yilari Giseth Melo Castaneda
# Salon-253

# Definimos la matriz con al menos 6 productos
# Cada fila es: Nombre- categoria- precio base.
menu =[
    ["Pizza", "Comida", 25000],
    ["Hamburguesa", "Comida", 15000],
    ["Jugo de mora", "Bebida", 3000],
    ["Gaseosa", "Bebida", 5000],
    ["Ensalada", "Comida", 16000],
    ["Postre", "Dulce", 8000]
]
# Ahoea definimos los criterios de la promocion 
categoria_objetivo = "Comida"
umbral_precio = 18000
descuento = 0.15 #15%

# Funcion para crear el precio final ya sea con descuento o sin el
def calcular_precio_final(categoria, precio):
    # Usamos if para verificar si cumple las los condiciones:
    # Categoria correcta y precio mayor umbral
    if categoria == categoria_objetivo and precio > umbral_precio:
        precio_final = precio - (precio * descuento)
    else:
        # Si no cumple, el precio se mantiene igual
        precio_final = precio
    return precio_final

# Ciclo for para recorrer cada producto de la matriz y mostrar resultados
print("--- MENÚ DE RESTAURANTE CON PROMOCIONES---")
# Ciclo for para recorrer la matriz
for producto in menu:
    # separamos los datos de cada fila
    nombre = producto[0]
    categoria = producto[1]
    precio = producto [2]
    
    # Calculamos el precio final usando la funcion
    resultado = calcular_precio_final(categoria, precio)
    
    # Imprimimos
    print("Producto:", nombre, "Categoria:", categoria, "Precio base:", precio, "Precio final:", resultado)
    