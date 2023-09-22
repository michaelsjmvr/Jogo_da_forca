import sys
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

class JogoDaForca(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações iniciais da janela principal
        self.setWindowTitle("Jogo da Forca")  # Define o título da janela
        self.setGeometry(100, 100, 400, 400)  # Define a posição e o tamanho da janela

        central_widget = QWidget(self)  # Cria um widget central para a janela
        self.setCentralWidget(central_widget)  # Define o widget central

        layout = QVBoxLayout(central_widget)  # Cria um layout de grade vertical para organizar os elementos

        # Configuração dos elementos da interface gráfica
        self.dica_label = QLabel("Dica: É uma linguagem de programação.", self)  # Rótulo para exibir a dica
        self.palavra_label = QLabel("", self)  # Rótulo para exibir a palavra com letras adivinhadas
        self.tentativas_label = QLabel("", self)  # Rótulo para exibir o número de tentativas restantes
        self.resultado_label = QLabel("", self)  # Rótulo para exibir mensagens de resultado

        self.letra_input = QLineEdit(self)  # Caixa de entrada para o jogador adivinhar letras
        self.adivinhar_button = QPushButton("Adivinhar", self)  # Botão para fazer adivinhações

        # Conexões de sinal e slot para o botão
        self.adivinhar_button.clicked.connect(self.verificar_letra)  # Conecta o botão ao método verificar_letra

        # Adiciona os elementos ao layout vertical
        layout.addWidget(self.dica_label)
        layout.addWidget(self.palavra_label)
        layout.addWidget(self.tentativas_label)
        layout.addWidget(self.resultado_label)
        layout.addWidget(self.letra_input)
        layout.addWidget(self.adivinhar_button)

        # Inicialização das variáveis do jogo
        self.palavra = self.escolher_palavra()  # Escolhe uma palavra aleatória
        self.letras_corretas = []  # Lista de letras adivinhadas corretamente
        self.tentativas = 6  # Número máximo de tentativas

        # Atualiza a interface gráfica inicial
        self.atualizar_interface()

    def escolher_palavra(self):
        # Lista de palavras possíveis para o jogo
        palavras = ["PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS", "RUBY"]
        return random.choice(palavras)  # Escolhe uma palavra aleatória da lista

    def exibir_palavra(self):
        resultado = ""
        for letra in self.palavra:
            if letra in self.letras_corretas:
                resultado += letra
            else:
                resultado += "_"
        return resultado

    def atualizar_interface(self):
        # Atualiza os rótulos da interface com informações do jogo
        self.dica_label.setText("Dica: É uma linguagem de programação.")
        self.palavra_label.setText("Palavra: " + self.exibir_palavra())
        self.tentativas_label.setText("Tentativas restantes: " + str(self.tentativas))
        self.resultado_label.setText("")

    def verificar_letra(self):
        letra = self.letra_input.text().upper()  # Obtém a letra digitada pelo jogador e a converte para maiúscula

        if letra in self.letras_corretas:
            # Se a letra já foi adivinhada corretamente, exibe uma mensagem
            self.mostrar_mensagem("Letra já adivinhada", "Você já adivinhou esta letra.")
            return

        if letra in self.palavra:
            # Se a letra está na palavra, adiciona à lista de letras corretas
            self.letras_corretas.append(letra)
        else:
            # Se a letra não está na palavra, decrementa o número de tentativas
            self.tentativas -= 1

        self.letra_input.clear()  # Limpa a caixa de entrada
        self.atualizar_interface()  # Atualiza a interface gráfica

        if self.exibir_palavra() == self.palavra:
            # Se todas as letras foram adivinhadas, o jogador venceu
            self.mostrar_mensagem("Parabéns!", "Você venceu! A palavra é: " + self.palavra)
        elif self.tentativas == 0:
            # Se o número de tentativas esgotou, o jogador perdeu
            self.mostrar_mensagem("Fim de jogo", "Você perdeu. A palavra era: " + self.palavra)

    def mostrar_mensagem(self, titulo, mensagem):
        # Exibe uma mensagem em uma caixa de diálogo
        mensagem_box = QMessageBox(self)
        mensagem_box.setWindowTitle(titulo)
        mensagem_box.setText(mensagem)
        mensagem_box.setStandardButtons(QMessageBox.Ok)
        mensagem_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Inicializa a aplicação Qt
    jogo = JogoDaForca()  # Cria uma instância da classe JogoDaForca
    jogo.show()  # Exibe a janela do jogo
    sys.exit(app.exec())  # Executa o loop de eventos da aplicação
