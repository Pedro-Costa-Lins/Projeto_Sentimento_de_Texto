
ArquivoFeliz = open(r"PalavrasRelacionadasFELICIDADE.txt","r")
ArquivoRaivoso = open(r"PalavrasRelacionadasRAIVA.txt","r")
ArquivoTriste = open(r"PalavrasRelacionadasTRSITEZA.txt","r")

def listador(TXT):
    Listagem = []
    for linha in TXT:
        Listagem.append(linha)
    return Listagem

ListaFeliz = listador(ArquivoFeliz)
ListaRaivosa = listador(ArquivoRaivoso)
ListaTriste = listador(ArquivoTriste)

Feliz = 0
Triste = 0
Raivoso = 0

texto = input("Escreva uma frase: ")

listinha = texto.split()

print(listinha)

print("-Finalizado-")