import time
import os
import pyautogui
import pyperclip  # Para copiar e colar a resposta do terminal
import json

def test_xterm_curl():
    os.environ["DISPLAY"] = ":99"  # Usa o display virtual do Xvfb

    # Verifica se o terminal já está aberto
    existing_process = os.popen("pgrep xterm").read()
    if not existing_process:
        os.system("xterm &")  
        time.sleep(5)  
        print("Terminal xterm foi aberto.")
    else:
        print("xterm já estava em execução.")

    time.sleep(2)

    # Comando cURL que será digitado no terminal
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"

    # Digita o comando
    pyautogui.write(curl_command, interval=0.05)
    print("Comando cURL digitado.")

    time.sleep(5)  # Aguarda antes de pressionar Enter

    # Pressiona Enter para executar
    pyautogui.press("enter")
    print("Comando cURL executado.")

    time.sleep(10)  # Espera a resposta aparecer no terminal

    # Copia a saída do terminal (Seleciona tudo e copia)
    pyautogui.hotkey("ctrl", "a")  # Seleciona tudo no terminal
    time.sleep(1)
    pyautogui.hotkey("ctrl", "c")  # Copia o conteúdo
    time.sleep(1)

    # Obtém a resposta copiada
    response_text = pyperclip.paste()
    print("Resposta copiada do terminal:", response_text)

    # Filtra o JSON dentro das chaves {}
    json_start = response_text.find("{")
    json_end = response_text.rfind("}") + 1
    json_string = response_text[json_start:json_end]

    # Converte para dicionário
    try:
        response_json = json.loads(json_string)
        success = response_json.get("success")
        status = response_json.get("status")
        message = response_json.get("message")

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
