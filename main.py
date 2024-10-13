
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
def almacenar_menos_kilos(nombre_granos:list, matriz:list):
    nombre_granos = crear_matriz(1,1,"Maiz, Trigo, Cebada, Centeno ")
    nombre_menor_grano = sumar_kilos(matriz)
    nombre_menor_ceral_por_deposito = []
  
    for j in range(len(nombre_granos[0])):#columnas
       
        for i in range(len(matriz[0])-1):#filas
            if matriz < nombre_menor_grano:
                nombre_menor_ceral_por_deposito += matriz[i][j]
              
                   
       
    return nombre_menor_ceral_por_deposito
        
                
               
                
        
    

matriz = crear_matriz(2,4,None)
cargar_matriz(matriz)
suma_fila = sumar_kilos(matriz)
print(f"Suma de la filas : {suma_fila}")

nombre_granos = almacenar_menos_kilos("", matriz)
print(f"El nombre del ceral con menos kilos es: {nombre_granos}")
# menor_kilo = almacenar_menos_kilos(nombre_granos)
# print(menor_kilo)




mostrar_matriz(matriz)  



 