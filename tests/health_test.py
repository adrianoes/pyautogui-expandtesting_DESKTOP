import time
import os
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

    # Comando cURL
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"

    # Executa o comando curl e redireciona a resposta diretamente para o clipboard
    os.system(f"{curl_command} | xclip -selection clipboard")

    # Agora, vamos pegar o conteúdo do clipboard
    response_from_clipboard = os.popen("xclip -selection clipboard -o").read().strip()  # Captura o conteúdo do clipboard

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
