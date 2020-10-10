def separadorDePalavras(Frase):
    Lista = Frase.split()
    return Lista

def comparador(Frase,Lista):
    for i in Lista:
        for j in Frase:
            if i == j:
                return True
    return False

Lista = separadorDePalavras(input("Escreva uma frase: "))

ListaNegativas = ['Não' , 'odeio' , 'morra' , 'idiota' , 'matar']

resultado = comparador(Lista,ListaNegativas)

print(resultado)

print("-Finalizado-")