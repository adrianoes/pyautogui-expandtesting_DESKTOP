import time
import os
import pyautogui
import json
import pyperclip
from faker import Faker

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

    # Comando cURL
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"

    # Digita e executa o comando cURL no terminal
    pyautogui.write(curl_command, interval=0.05)
    print("Comando cURL digitado.")
    time.sleep(5)
    pyautogui.press("enter")
    print("Comando cURL executado.")

    time.sleep(10)  # Aguarda a resposta ser impressa no terminal

    # Seleciona todo o conteúdo do terminal
    pyautogui.hotkey("ctrl", "shift", "a")
    time.sleep(2)

    # Copia para a área de transferência
    pyautogui.hotkey("ctrl", "shift", "c")
    time.sleep(2)

    # Obtém o conteúdo da área de transferência
    response_text = pyperclip.paste().strip()
    print("Resposta copiada do terminal:", response_text)

    # Gera um nome aleatório para a variável
    faker = Faker()
    randomVarName = f"data_{faker.hexify(text='^^^^^^^^^^^^')}"  # Exemplo: "data_a1b2c3d4e5f6"

    try:
        # Converte para dicionário JSON
        response_json = json.loads(response_text)
        success = response_json.get("success")
        status = response_json.get("status")
        message = response_json.get("message")

        # Armazena os valores na variável aleatória
        globals()[randomVarName] = {
            "success": success,
            "status": status,
            "message": message
        }

        print(f"Dados extraídos: success={success}, status={status}, message='{message}'")
        print(f"Dados armazenados na variável aleatória: {randomVarName}")

        # Assertions
        assert success == True, "Erro: success não é True"
        assert status == 200, "Erro: status não é 200"
        assert message == "Notes API is Running", "Erro: mensagem incorreta"

        print("✅ Teste passou com sucesso!")

    except json.JSONDecodeError:
        print("❌ Erro ao converter a resposta para JSON!")

# Executa o teste
test_xterm_curl()
