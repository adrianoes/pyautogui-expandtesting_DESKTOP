import time
import pyautogui
import os
import json

def test_xterm_curl():
    os.environ["DISPLAY"] = ":99"  # Usa o display virtual do Xvfb

    # Verifica se o terminal já está aberto
    existing_process = os.popen("pgrep xterm").read()
    if not existing_process:
        os.system("xterm &")  
        time.sleep(5)  # Espera o terminal abrir
        print("Terminal xterm foi aberto.")
    else:
        print("xterm já estava em execução.")

    # Aguarda o terminal abrir completamente
    time.sleep(2)

    # Maximiza a janela do terminal com o atalho Fn + Alt + F10
    pyautogui.hotkey("fn", "alt", "f10")  # Maximiza a janela
    time.sleep(2)  # Espera um pouco para garantir que a janela foi maximizada

    # Dá o foco ao terminal (usando Alt+Tab ou qualquer outra abordagem, dependendo do sistema)
    pyautogui.hotkey("alt", "tab")  # Foca no terminal
    time.sleep(1)  # Aguarda um pouco para garantir o foco no terminal

    # Espera mais um pouco para garantir que o terminal esteja pronto para receber o comando
    time.sleep(2)

    # Comando cURL
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"

    # Escreve o comando cURL no terminal com mais intervalo para evitar erros de digitação
    pyautogui.write(curl_command, interval=0.2)  # Aumentamos o intervalo para 0.2s
    pyautogui.press("enter")  # Executa o comando no terminal
    print("Comando cURL executado.")

    # Espera mais tempo para garantir que a resposta apareça corretamente no terminal
    time.sleep(6)  # Ajuste o tempo se necessário, dependendo da resposta da API

    # Seleção do conteúdo no terminal: clicando 3 vezes na posição x=703, y=40
    pyautogui.click(703, 40)  # Clica na posição inicial
    time.sleep(0.5)  # Aguarda um pouco
    pyautogui.click(703, 40)  # Clica novamente
    time.sleep(0.5)  # Aguarda um pouco
    pyautogui.click(703, 40)  # Clica pela terceira vez
    time.sleep(0.5)  # Aguarda para garantir que o texto está selecionado

    # Copia a seleção usando o atalho Ctrl + Shift + C
    pyautogui.hotkey("ctrl", "shift", "c")  # Copia a seleção
    time.sleep(1)  # Aguarda um pouco para garantir que a cópia foi feita

    # Agora, o conteúdo está no clipboard, vamos capturá-lo
    os.system("xclip -selection clipboard -o > clipboard_output.txt")  # Usa xclip para salvar a resposta em um arquivo temporário

    # Lê o conteúdo do arquivo temporário
    with open('clipboard_output.txt', 'r') as file:
        response_from_clipboard = file.read().strip()

    # Exibe a resposta copiada
    print(f"Resposta copiada do clipboard: {response_from_clipboard}")

    # Converte a resposta para JSON
    try:
        response_json = json.loads(response_from_clipboard)
        success = response_json.get("success")
        status = response_json.get("status")
        message = response_json.get("message")

        # Exibe os dados extraídos
        print(f"Dados extraídos: success={success}, status={status}, message='{message}'")

        # Assertions
        assert success == True, "Erro: success não é True"
        assert status == 200, "Erro: status não é 200"
        assert message == "Notes API is Running", "Erro: mensagem incorreta"

        print("✅ Teste passou com sucesso!")

    except json.JSONDecodeError:
        print("❌ Erro ao converter a resposta para JSON!")

# Executa o teste
test_xterm_curl()
