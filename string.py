
concatenacao = ""

while True:
    palavra = input("digite uma palavra: ")
    if palavra == "/exit" :
        break
    else:
        concatenacao = concatenacao + " " + palavra

print(concatenacao)

