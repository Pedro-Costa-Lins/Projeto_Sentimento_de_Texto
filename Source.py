#Abre os documentos de texto para análise.
ArquivoFeliz   = open(r"PalavrasRelacionadasFELICIDADE.txt","r")
ArquivoRaivoso = open(r"PalavrasRelacionadasRAIVA.txt","r")
ArquivoTriste  = open(r"PalavrasRelacionadasTRISTEZA.txt","r")

#Transforma cada documento de texto em uma lista de palavras.
def listador(TXT):
    Listagem = []
    for linha in TXT:
        Listagem.append(linha.rstrip())
    return Listagem

#Cada grupo de palavras separado na lista adequada.
ListaFeliz   = listador(ArquivoFeliz)
ListaRaivosa = listador(ArquivoRaivoso)
ListaTriste  = listador(ArquivoTriste)

#Input inicial a ser comparado.
texto = input("Escreva uma frase: ")

#Tranforma a frase numa lista.
Listinha = texto.split()

def veredito():
    #Acumuladores para contabilizar a aparição de palavras que representem certo sentimento.
    PtsFelizes  = 0
    PtsRaivosos = 0
    PtsTristes  = 0
    Encontrado  = False
    #Uma sequencia de comparações para preencher os acumuladores
    for palavra in Listinha:
        Encontrado = False
        for comparada in ListaFeliz:
            if palavra.casefold() == comparada.casefold():
                PtsFelizes += 1
                Encontrado = True
                break
        if Encontrado == False:
            for comparada in ListaRaivosa:
                if palavra.casefold() == comparada.casefold():
                    PtsRaivosos += 1
                    Encontrado = True
                    break
        if Encontrado == False:
            for comparada in ListaTriste:
                if palavra.casefold() == comparada.casefold():
                    PtsTristes += 1
                    break

    #Uma avaliação das pontuações e a declaração da maior        
    if PtsFelizes > PtsRaivosos and PtsFelizes > PtsTristes:
        return "Felicidade"
    elif PtsRaivosos > PtsFelizes and PtsRaivosos > PtsTristes:
        return "Raiva"
    elif PtsTristes  > PtsFelizes and PtsTristes > PtsRaivosos:
        return "Tristeza"
    else:
        return "Inconclusivo"

print(veredito())

print("-Finalizado-")