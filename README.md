# Jogo da Forca em PySide6

## Autor: Michael Douglas P Lima
## Contato: michaelsjmvr@hotmail.com
## LinkedIn: [michael-douglas-640a11180](https://www.linkedin.com/in/michael-douglas-640a11180/)

## Descrição do Projeto
Este é um projeto de um jogo da forca desenvolvido em Python com a biblioteca PySide6 para criar a interface gráfica. O jogo consiste em adivinhar uma palavra oculta e tem como objetivo principal a prática da programação com PySide6.

## Estrutura do Projeto
O projeto é composto por uma única classe chamada JogoDaForca, que herda de QMainWindow. A interface gráfica é construída usando elementos do PySide6, como rótulos, caixas de entrada e botões. Aqui está uma visão geral da estrutura do projeto:

- **Importação de módulos e bibliotecas necessários:**
  - sys: Para interagir com o sistema operacional.
  - random: Para escolher uma palavra aleatória para o jogo.
  - Classes do PySide6: Para criar a interface gráfica.

- **JogoDaForca (classe principal):**
  - Configurações iniciais da janela principal, como título e tamanho.
  - Criação de elementos da interface, como rótulos, caixa de entrada e botão.
  - Conexão do botão "Adivinhar" a um método (verificar_letra) para tratar as adivinhações do jogador.
  - Métodos para escolher uma palavra aleatória, exibir a palavra oculta, atualizar a interface, verificar letras e mostrar mensagens de resultado.
  - Inicialização das variáveis do jogo, como a palavra oculta, letras corretas e tentativas.

- **Método escolher_palavra:**
  - Retorna uma palavra aleatória escolhida a partir de uma lista predefinida de palavras.

- **Método exibir_palavra:**
  - Gera uma representação da palavra oculta com letras adivinhadas pelo jogador.

- **Método atualizar_interface:**
  - Atualiza os rótulos da interface gráfica com informações relevantes, como dicas, palavra oculta e tentativas restantes.

- **Método verificar_letra:**
  - Obtém a letra digitada pelo jogador.
  - Verifica se a letra já foi adivinhada corretamente.
  - Verifica se a letra está na palavra oculta.
  - Atualiza as letras adivinhadas e as tentativas.
  - Verifica se o jogador venceu ou perdeu o jogo.

- **Método mostrar_mensagem:**
  - Exibe mensagens em uma caixa de diálogo para informar o jogador sobre o resultado do jogo.

## Funcionamento do Jogo
- Ao iniciar o jogo, o jogador recebe uma dica sobre a palavra a ser adivinhada.
- A interface exibe a palavra oculta com espaços para as letras e um contador de tentativas restantes.
- O jogador pode digitar uma letra na caixa de entrada e pressionar o botão "Adivinhar".
- Se a letra estiver correta, ela é exibida na palavra oculta. Caso contrário, o contador de tentativas é decrementado.
- O jogo continua até que o jogador adivinhe corretamente todas as letras da palavra ou até que as tentativas se esgotem.
- O jogador recebe uma mensagem informando se ganhou ou perdeu o jogo.

## Execução
O código finaliza com a inicialização de uma instância da classe JogoDaForca e a execução da aplicação Qt. A janela do jogo é exibida, permitindo que o jogador interaja com a interface gráfica e jogue o jogo da forca.
