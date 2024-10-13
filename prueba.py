def almacenar_menos_kilos(nombre_granos:list, matriz:list):
    # nombre_granos = crear_matriz(1,1,"Maiz, Trigo, Cebada, Centeno ")
    # nombre_menor_grano = sumar_kilos(matriz)
    nombre_menor_ceral_por_deposito = [""]
    nombre_menor_grano = 0
    for j in range(len(nombre_granos[0])):#columnas
        if  matriz[i][j] < nombre_menor_grano:
            nombre_menor_grano = matriz[i][j]
        for i in range(len(matriz)):#filas
            if matriz< nombre_menor_grano:
                nombre_menor_ceral_por_deposito = nombre_menor_grano
            
       
            nombre_menor_ceral_por_deposito += [nombre_menor_grano]    
    return nombre_menor_ceral_por_deposito

# Ejemplo de uso:
cereales = ["Maíz", "Trigo", "Cebada", "Centeno"]
matriz = [
    [100, 200, 150,10],  # Maíz 460
    [80, 250, 100, 10],   # Trigo 440
    [120, 180, 90, 10],   # Cebada 400
    [110, 170, 140, 10]   # Centeno 430
]

resultado = almacenar_menos_kilos(cereales, matriz)
print(resultado)  # ['Trigo', 'Centeno', 'Cebada']



# def listar_nombres_cereal(matriz: list, nombres:str)->list:
#     """Lista nombres

#     Args:
#         matriz (list): crea matriz

#     Returns:
#         list: lista nombre
#     """
 
#     for i in range(len(matriz)):
#         nombres += matriz[i]
#     return nombres


# matriz = [ "MAIZ, TRIGO, CEBADA, CENTENO"]
# print(matriz)

# 
# def listar_nombres_cereal(matriz: list, nombres:str)->list:
#     """Lista nombres

#     Args:
#         matriz (list): crea matriz

#     Returns:
#         list: lista nombre
#     """
 
#     for i in range(len(matriz)):
#         nombres += matriz[i]
#     return nombres


# nombre_granos = almacenar_menos_kilos(matriz)
# print(nombre_granos)
#istar_nombres = listar_nombres_cereal(matriz, "MAIZ, TRIGO, CEBADA, CENTENO")
# print(listar_nombres)