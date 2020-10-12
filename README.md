# Project_Text_Sentiment
Este programa tem o objetivo de avaliar o sentimento de uma frase dentre Felicidade, Raiva e Tristeza.

A ideia básica é que ele compara as palavras da frase com listas de palavras correspondentes a cada sentimento, havendo um sentimento dominante, o mesmo será apresentado como retorno.

As listas de palavras foram obtidas no site https://dicionariocriativo.com.br/

Será agora mencionada o índice da parte do código a qual se pretende dissertar.

=(01) São abertos os documentos de texto que correspondem as listas de palavras.
=(02) Listas são criadas a partir da função (FnO1) usando os documentos de texto.
=(03) Recebe um input de usuário, transforma o mesmo numa lista através da função(Fn02), e devolve a resposta junto a uma frase que a especifica.

=(Fn01) Cria uma lista, e irá adicionar na mesma cada linha individual, sem contar o caractere "\n".

=(Fn02) Recebe uma frase, a separa numa lista usando os espaços como divisores, a variável "Adicionado" registra se houve uma interação do código com uma vírgula e seu estado inicial é "False". Se inicia um laço no tamanho da lista (quantidade de palavras) com a variável "i" servindo de controle em formato de inteiro. De imediato se verifica o estado da variável "Adicionado", se o estado da mesma for "true", ele será resetado e a pulará para a próxima iteração do laço, senão, será verificado se o último caractere é uma vírgula, sendo ele, a vírgula será removida e adicionada a lista como um termo independente logo após. O mesmo acontece com ".". Retorna a lista.

=(Fn03) Vai avaliar o texto de acordo com a lógica programada e as listas de palavras relacionadas a sentimentos.
-(Fn03.1) Cria 3 variáveis acumuladoras que servirão para calcular a quantidade de sentimento na frase e dois booleanos de controle que ajudarão na interpretação do texto.
-(Fn03.2) Vai iterar entre a palavras do texto do usuário. Restar o booleano de controle "Encontrado", que diz se já houve uma palavra compatível numa lista, permitindo o código a passar para a próxima palavra. Verifica se houve uma vírgula, a qual se for encontrada cancela o efeito negativo que uma palavra "não" ou "nem" pode ocasionar numa palavra que seja compatível num sentimento.
-(Fn03.3) Ao encontrar uma das palavras citadas, ativa um efeito de negação que vai contar negativamente na pontuação da próxima palavra de sentimento encontrada. E imediatamente passa para a próxima palavra.
-(Fn03.4) Um comparador que procura se uma palavra está dentro de uma das listas, levando em consideração se existe uma negação e pontuando de acordo, e ao encontrar uma palavra o mesmo encerra a iteração própria e impede que a mesma palavra seja considerada em outras listas.
-(Fn03.5) São comparadas as pontuações relacionadas com cada sentimento, e se existir uma predominância, a mesma será dada como resposta, caso contrário, o resultado é inconclusivo.
