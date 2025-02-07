import time
import pyautogui
import os
import json

def test_xterm_curl():
    os.environ["DISPLAY"] = ":99"

    # Verifica se o terminal já está aberto
    existing_process = os.popen("pgrep xterm").read().strip()
    
    if not existing_process:
        print("Abrindo novo terminal xterm...")
        os.system("xterm -fa 'Monospace' -fs 12 &")  # Forçando uma fonte padrão para evitar erros
        time.sleep(5)  # Espera o terminal abrir
    else:
        print(f"xterm já estava em execução (PID: {existing_process}). Não abrindo novo terminal.")

    # Aguarda o terminal abrir completamente
    time.sleep(2)

    # Garante que o terminal tenha foco
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    # Verifica se já há um script de captura ativo (evita redirecionamento duplicado)
    if not os.path.exists("/tmp/last"):
        print("Configurando captura de saída do terminal...")
        save_output_script = """trap 'echo "capturando saída..." > /tmp/last' DEBUG"""
        pyautogui.write(save_output_script, interval=0.1)
        pyautogui.press("enter")
        time.sleep(2)  # Aguarda mais tempo para garantir que o redirecionamento seja configurado
    else:
        print("Captura de saída já configurada. Pulando essa etapa.")

    # Comando cURL
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    
    pyautogui.write(curl_command, interval=0.15)
    pyautogui.press("enter")
    print("Comando cURL executado.")

    # Espera adicional para garantir que o comando cURL seja processado
    time.sleep(10)  # Aumenta o tempo de espera

    # Verifica a resposta no arquivo /tmp/last
    response_from_file = ""
    retry_count = 0
    max_retries = 10

    while retry_count < max_retries:
        if os.path.exists("/tmp/last") and os.path.getsize("/tmp/last") > 0:
            with open("/tmp/last", "r") as file:
                response_from_file = file.read().strip()
            if response_from_file:
                break  # Sai do loop assim que encontrar conteúdo
        print(f"Tentativa {retry_count + 1}: Arquivo /tmp/last ainda vazio, aguardando...")
        time.sleep(3)  # Aumenta o tempo de espera entre as tentativas
        retry_count += 1

    print(f"Resposta capturada: {response_from_file}")

    # Se a resposta foi capturada, tentamos decodificar em JSON
    if response_from_file:
        try:
            response_json = json.loads(response_from_file)
            success = response_json.get("success")
            status = response_json.get("status")
            message = response_json.get("message")

            print(f"Dados extraídos: success={success}, status={status}, message='{message}'")

            assert success == True, "Erro: success não é True"
            assert status == 200, "Erro: status não é 200"
            assert message == "Notes API is Running", "Erro: mensagem incorreta"

            print("✅ Teste passou com sucesso!")

        except json.JSONDecodeError:
            print("❌ Erro ao converter a resposta para JSON!")
    else:
        print("❌ A resposta não foi capturada corretamente.")

    # Fecha o terminal após capturar a resposta
    os.system("pkill xterm")
