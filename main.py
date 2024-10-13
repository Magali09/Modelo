
# cereales en el interior del país. Para ello cuentan con 20 depósitos en CABA,
# que generalmente se encuentran en las inmediaciones de las estaciones del
# ferrocarril.
# Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo, cebada y centeno.
# La oficina central, recibe mensualmente una planilla de existencias donde se
# indican las existencias de cada cereal para cada depósito.
# Realizar un menú de opciones:
# 1. Obtener existencias: para ello deberá crear una función que cargue la
# existencia de cada grano en todos los depósitos. Los valores estarán
# comprendidos entre 5000 Kg y 20000 Kg.

def crear_matriz(cantidad_filas:int, cantidad_columnas:int, valor:any)->list:
    """crea matriz

    Args:
        cantidad_filas (int): cantidad fila
        cantidad_columnas (int): cantidad columnas
        valor (any): cualquier valor

    Returns:
        list: crea matriz
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list)->None:
    """muestra matiz

    Args:
        matriz (list): muestra matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()

def cargar_matriz(matriz:list)->None:
    """cargo secuencialmente matriz

    Args:
        matriz (list): cargo secuencialmente matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            granos = int(input("Ingrese candidad de Kilos entre 5000 y 20000: "))
            while granos < 5000 or granos > 20000:
                granos = int(input("Reingrese candidad de Kilos entre 5000 y 20000: "))
            matriz[i][j] = granos
                
# 2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales.

def sumar_kilos(matriz: list) -> list:
    """Suma los valores de una fila de la matriz.

    Args:
        matriz (list): matriz de la cual sumar los kilos
        fila (int): índice de la fila a sumar

    Returns:
        int: suma de los valores en la fila especificada
    """
    lista_suma = []
    for fila in range(len(matriz)):
        suma = 0
        for i in range(len(matriz[fila])):
            suma += matriz[fila][i]
        lista_suma += [suma]
    return lista_suma
        

# 3. Nombre del cereal que almaceno menos kilos en cada depósito.
def almacenar_menos_kilos(matriz:list):
    nombre_granos = crear_matriz(1,4,"")
    nombre_granos[0][0] = "Maiz"
    nombre_granos[0][1] = "Centeno"
    nombre_granos[0][2] = "Cebada"
    nombre_granos[0][3] = "gfvgvb"
    
    nombre_menor_ceral_por_deposito = []
    cereales_menor_valor = []
  
    for i in range(len(matriz)):#filas
        cereal_menor_valor = 90000
        menor_valor_deposito = matriz[i][0]
        for j in range(len(nombre_granos[0])):#columnas
            if matriz[i][j] < menor_valor_deposito:
                menor_valor_deposito = matriz[i][j]
                cereal_menor_valor = nombre_granos[0][j]

        nombre_menor_ceral_por_deposito  = nombre_menor_ceral_por_deposito + [menor_valor_deposito]
        cereales_menor_valor =   cereales_menor_valor +[cereal_menor_valor]

    for i in range(len(cereales_menor_valor)):
        print(cereales_menor_valor[i])          
    return nombre_menor_ceral_por_deposito
        
                
               

# 4. Máxima cantidad de kilos almacenados de cada cereal.              
def almacenar_mayor_kilos(matriz:list):
    nombre_granos = crear_matriz(1,4,"")
    nombre_granos[0][0] = "Maiz"
    nombre_granos[0][1] = "Centeno"
    nombre_granos[0][2] = "Cebada"
    nombre_granos[0][3] = "gfvgvb"
    
    nombre_menor_ceral_por_deposito = []
    cereales_menor_valor = []
    for i in range(len(matriz)):#filas
        cereal_menor_valor = 0
        menor_valor_deposito = matriz[i][0]
        for j in range(len(nombre_granos[0])):#columnas
            if matriz[i][j] > menor_valor_deposito:
                menor_valor_deposito = matriz[i][j]
                cereal_menor_valor = nombre_granos[0][j]

        nombre_menor_ceral_por_deposito  = nombre_menor_ceral_por_deposito + [menor_valor_deposito]
        cereales_menor_valor = cereales_menor_valor + [cereal_menor_valor]

    for i in range(len(cereales_menor_valor)):
        print(cereales_menor_valor[i])          
    return nombre_menor_ceral_por_deposito    
    

matriz = crear_matriz(2,4,None)
cargar_matriz(matriz)
suma_fila = sumar_kilos(matriz)
print(f"Suma de la filas : {suma_fila}")


menor_kilo = almacenar_menos_kilos(matriz)
print(menor_kilo)
mayor_kilo = almacenar_mayor_kilos(matriz)
print(mayor_kilo)
mostrar_matriz(matriz)  



 