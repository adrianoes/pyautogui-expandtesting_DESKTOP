import time
import os

def test_open_xterm():
    # Configura a variável DISPLAY para usar o ambiente virtual do Xvfb
    os.environ["DISPLAY"] = ":99"  # Isso garante que o xterm será exibido no display virtual do Xvfb

    # Tenta abrir o terminal diretamente com o comando "xterm"
    os.system("xterm &")  # Abre o terminal xterm diretamente
    time.sleep(5)  # Espera o terminal abrir

    # Exibe uma mensagem de sucesso
    print("Terminal xterm foi aberto.")

# Execute a função para testar
test_open_xterm()
