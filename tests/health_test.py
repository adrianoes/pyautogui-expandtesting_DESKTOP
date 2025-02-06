import time
import os

def test_open_xterm():
    # Configura a variável DISPLAY para usar o ambiente virtual do Xvfb
    os.environ["DISPLAY"] = ":99"  # Isso garante que o xterm será exibido no display virtual do Xvfb

    # Verifica se o processo xterm já está em execução
    existing_process = os.popen("pgrep xterm").read()
    if not existing_process:
        # Abre o terminal xterm diretamente
        os.system("xterm &")  # Abre o terminal xterm diretamente
        time.sleep(5)  # Espera o terminal abrir
        print("Terminal xterm foi aberto.")
    else:
        print("xterm já está em execução.")

# Execute a função para testar
test_open_xterm()
