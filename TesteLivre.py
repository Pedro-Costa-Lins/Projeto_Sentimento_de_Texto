#Lugar para teste de código sem compromisso.

texto = input("Escreva uma frase: ")

#Tranforma a frase numa lista, remove vírgulas de palavras que terminam com as mesmas e adiciona a vírgula como parte idempendente da lista.
def formatador(texto):
    Lista = texto.split()
    Adicionado = False
    for i in range(len(Lista)):
        if Adicionado:
            Adicionado = False
            continue
        if Lista[i][-1] == ",":
            Lista[i] = Lista[i].replace(",", "")
            Lista.insert(i + 1, ",")
            Adicionado = True
    return Lista

print(formatador(texto))