import random
 
filas= input("ingrese un numero de filas:")
columnas= input("ingrese un numero de columnas:")    
m1= [[1,2,3],[4,5,6]]

M1= [[random.randint(0,5)for j in range (columnas) for i in range(filas)]]
M2= [[random.randint(0,5)for j in range (columnas) for i in range(filas)]]

for i in range(filas):
    for j in range(columnas):
        M1[i][j] == int(input(f"Matriz ({i+1}, {j+1}):"))
   
for i in range(filas):
    for j in range (columnas):
        M2[i][j] == int(input(f"Matriz({i+1},{j+1}):"))

print(m1)

