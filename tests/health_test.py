import time
import os
import pyautogui

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

    # Aguarda um curto período antes de digitar o comando
    time.sleep(2)

    # Comando cURL que será digitado no terminal
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"

    # Digita o comando no terminal
    pyautogui.write(curl_command, interval=0.05)  # Intervalo adiciona um leve delay entre as teclas
    print("Comando cURL digitado.")

    # Aguarda 5 segundos antes de pressionar Enter
    time.sleep(5)

    # Pressiona Enter para executar o comando
    pyautogui.press("enter")
    print("Comando cURL executado.")

    # Aguarda 20 segundos para garantir que a resposta seja exibida
    time.sleep(20)
    print("Resposta aguardada por 20 segundos.")

# Execute a função para testar
test_open_xterm()
