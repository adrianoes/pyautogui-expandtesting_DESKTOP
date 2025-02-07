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

    # Comando cURL
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"

    # Escreve o comando cURL no terminal
    pyautogui.write(curl_command)
    pyautogui.press("enter")  # Executa o comando no terminal
    print("Comando cURL executado.")

    # Espera alguns segundos para a resposta aparecer no terminal
    time.sleep(5)  # Ajuste o tempo se necessário

    # Simula a seleção do conteúdo do terminal usando o atalho 'Ctrl+Shift+A'
    pyautogui.hotkey("ctrl", "shift", "a")  # Seleciona todo o conteúdo do terminal
    time.sleep(1)  # Espera a seleção ser feita

    # Copia o conteúdo selecionado para o clipboard
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
