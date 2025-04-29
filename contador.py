contador = 0
while True:
    print("CONTADOR =",contador, end=" ")
    usuario=str(input('Deseja incrementar uma unidade? Y/N '))
    
    if usuario == "N":
        break
    elif usuario == "Y":
        contador+=1
    else:
        print("responde direito")