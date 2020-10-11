#Lugar para teste de código sem compromisso.

texto = input("Escreva uma frase: ")

#Tranforma a frase numa lista, remove vírgulas de palavras que terminam com as mesmas e adiciona a vírgula como parte idempendente da lista.
Listinha = texto.split()

Adicionado = False
for i in range(len(Listinha)):
    if Adicionado:
        Adicionado = False
        continue
    if Listinha[i][-1] == ",":
        Listinha[i].replace(",", "")
        Listinha.insert(i + 1, ",")
        Adicionado = True

print(Listinha)
