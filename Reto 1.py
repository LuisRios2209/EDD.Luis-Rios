palabra= input( "ingrese una palabra que contenga vocales:")
vocales= ("a,e,i,o,u")

contador= palabra.lower()
contador_a=0
contador_e=0
contador_i=0
contador_o=0
contador_u=0

for letras in palabra:
 if letras ==  "a":
    contador_a +=1
 elif letras == "e":
    contador_e +=1
 elif letras == "i":
    contador_i +=1
 elif letras == "o":
    contador_o +=1
 elif letras == "u":
    contador_u +=1

print(f"la palabra (palabra) tiene la cantida de:")
print(f"tiene {contador_a} A")
print(f"tiene {contador_e} E")
print(f"tiene {contador_i} I")
print(f"tiene {contador_o} O")
print(f"tiene {contador_u} U")
