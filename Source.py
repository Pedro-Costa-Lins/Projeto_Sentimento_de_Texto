#--==<Abre os documentos de texto para análise.>==--
ArquivoFeliz   = open(r"PalavrasRelacionadasFELICIDADE.txt","r")
ArquivoRaivoso = open(r"PalavrasRelacionadasRAIVA.txt","r")
ArquivoTriste  = open(r"PalavrasRelacionadasTRISTEZA.txt","r")

#Transforma cada documento de texto em uma lista de palavras.>==--
def listador(txt):
    Listagem = []
    for linha in txt:
        Listagem.append(linha.rstrip())
    return Listagem

#--==<Tranforma a frase numa lista, remove vírgulas de palavras que terminam com as mesmas e adiciona a vírgula como parte idempendente da lista.>==--
def formatador(texto):
    Lista = texto.split()
    Adicionado = False
    for i in range(len(Lista)):
        if Adicionado:
            Adicionado = False
            continue
        if Lista[i][-1] == ",":
            Lista[i].replace(",", "")
            Lista.insert(i + 1, ",")
            Adicionado = True
    return Lista

#--==<Cada grupo de palavras separado na lista adequada.>==--
ListaFeliz   = listador(ArquivoFeliz)
ListaRaivosa = listador(ArquivoRaivoso)
ListaTriste  = listador(ArquivoTriste)

#--==<Avalia a frase e devolve um resultado.>==--
def veredito():
    #Acumuladores para contabilizar a aparição de palavras que representem certo sentimento.
    PtsFelizes  = 0
    PtsRaivosos = 0
    PtsTristes  = 0
    Encontrado  = False
    Negação     = False
    
    #Uma sequencia de comparações para preencher os acumuladores
    for palavra in Listinha:
        #Reseta o boleano de controle.
        Encontrado = False
        
        #Se uma virgula for encontrada, a negação perde o efeito.
        if palavra == ",":
            Negação = False 
        
        #Ao ser identificada, a próxima palavra que expressar sentimento antes de uma vírgula vai ter um efeito negativo na pontuação de sentimento.
        #De imediato começa a análise da próxima palavra.
        if palavra.casefold() == "não" or palavra.casefold() == "nem":
            Negação = True
            continue
        
        #Comparador.
        for comparada in ListaFeliz:
            if palavra.casefold() == comparada.casefold():
                if Negação:
                    PtsFelizes -= 1
                    Encontrado  = True
                    Negação     = False
                    break
                else:
                    PtsFelizes += 1
                    Encontrado  = True
                    break
        if Encontrado == False:
            for comparada in ListaRaivosa:
                if palavra.casefold() == comparada.casefold():
                    if Negação:
                        PtsRaivosos -= 1
                        Encontrado   = True
                        Negação      = False
                        break
                    else:
                        PtsRaivosos += 1
                        Encontrado   = True
                        break
        if Encontrado == False:
            for comparada in ListaTriste:
                if palavra.casefold() == comparada.casefold():
                    if Negação:
                        PtsTristes -= 1
                        Negação     = False
                        break
                    else:
                        PtsTristes += 1
                        break
    #Mostra a pontuação



    #Uma avaliação das pontuações e a declaração da maior        
    if PtsFelizes > PtsRaivosos and PtsFelizes > PtsTristes:
        return "Felicidade"
    elif PtsRaivosos > PtsFelizes and PtsRaivosos > PtsTristes:
        return "Raiva"
    elif PtsTristes  > PtsFelizes and PtsTristes > PtsRaivosos:
        return "Tristeza"
    else:
        return "Inconclusivo"

#--==<Input inicial a ser comparado.>==--
texto = input("Escreva uma frase: ")

Listinha = formatador(texto)

print(veredito())

print("-Finalizado-")