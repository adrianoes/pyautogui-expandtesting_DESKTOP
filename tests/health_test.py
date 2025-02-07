import time
import os
import pyautogui
import json
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

    # Gera um nome aleatório para o arquivo JSON
    randomData = Faker().hexify(text='^^^^^^^^^^^^')  # Ex: "a1b2c3d4e5f6"
    json_filename = f"./resources/test_data_{randomData}.json"

    # Garante que o diretório resources existe
    os.makedirs("./resources", exist_ok=True)

    # Comando cURL que será digitado no terminal, redirecionando a saída para um arquivo
    curl_command = f"curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json' > {json_filename}"

    # Digita o comando
    pyautogui.write(curl_command, interval=0.05)
    print("Comando cURL digitado.")

    time.sleep(5)  # Aguarda antes de pressionar Enter

    # Pressiona Enter para executar
    pyautogui.press("enter")
    print("Comando cURL executado.")

    time.sleep(10)  # Espera a resposta ser gravada no arquivo

    # Lê o conteúdo do arquivo
    try:
        with open(json_filename, "r") as file:
            response_text = file.read().strip()
            print("Resposta capturada do terminal:", response_text)

        # Converte para dicionário
        response_json = json.loads(response_text)
        success = response_json.get("success")
        status = response_json.get("status")
        message = response_json.get("message")

        print(f"Dados extraídos: success={success}, status={status}, message='{message}'")

        # Assertions
        assert success == True, "Erro: success não é True"
        assert status == 200, "Erro: status não é 200"
        assert message == "Notes API is Running", "Erro: mensagem incorreta"

        print("✅ Teste passou com sucesso!")

    except (json.JSONDecodeError, FileNotFoundError):
        print("❌ Erro ao converter a resposta para JSON ou arquivo não encontrado!")

# Executa o teste
test_xterm_curl()
