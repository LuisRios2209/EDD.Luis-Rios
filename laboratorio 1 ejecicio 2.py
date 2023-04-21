
filas= input("ingrese un numero de filas:")
columnas= input("ingrese un numero de columnas:") 



for i in range (filas):
    for j in range(columnas):
        m1=[i][j]=int(input(f"Elemento({i+1}, {j+1}):"))

