Por: Marcelo Telles, Milton Bortolanza e Samuel Watthier

Nosso trabalho de Laboratório de Algoritmos II tem como objetivo desenvolver uma réplica do jogo Termo. No jogo, contem as opções de jogabilidade solo, dueto e quarteto.

Durante o jogo, o usuário irá digitar palavras de 5 caracteres. Se a letra estiver na posição correta, ela será exibida em verde; se o caractere estiver na palavra, mas não na posição correta, será exibido em amarelo; e se o caractere não estiver na palavra, será exibido em branco.

Utilizamos métodos como funções, modularização, manipulação de arquivos e a biblioteca nativa do Python.

No arquivo main.py, importamos nossos diversos módulos, nos quais a função principal contém todos os chamados do código.

Em menu.py, colocamos todas as opções de menu que fazem parte do jogo Termo.

Em wordlesolo.py, está o módulo que contém a versão solo do jogo, onde o usuário deve adivinhar uma palavra de 5 caracteres gerada aleatoriamente, possuindo 5 tentativas.

Em wordleduo.py, encontra-se a versão de dueto do jogo, onde o usuário deve adivinhar duas palavras simultaneamente, com direito a 5 tentativas.

Em wordlequad.py, está a versão de quarteto do jogo, onde o usuário deve acertar 4 palavras simultaneamente, tendo 9 tentativas.

No módulo words.py, randomizamos as palavras para que o usuário receba uma palavra diferente sempre que jogar.

Criamos um módulo com a função de limpar o console, de modo que em determinadas partes do código, o terminal seja limpo automaticamente, evitando uma tela tão poluída para o usuário.

Criamos um arquivo wordsintxt.txt, onde estão armazenadas nossas palavras, e excludedword.txt, para onde as palavras usadas são enviadas, garantindo que elas não se repitam no jogo.
