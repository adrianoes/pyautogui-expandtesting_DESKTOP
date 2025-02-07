import time
import pyautogui
import os
import json

def test_xterm_curl():
    os.environ["DISPLAY"] = ":99"

    existing_process = os.popen("pgrep xterm").read().strip()
    
    if not existing_process:
        print("Abrindo novo terminal xterm...")
        os.system("xterm &")
        time.sleep(5)
    else:
        print(f"xterm já estava em execução (PID: {existing_process}). Não abrindo novo terminal.")

    time.sleep(2)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    if not os.path.exists("/tmp/last"):
        print("Configurando captura de saída do terminal...")
        save_output_script = """exec 3>&1; trap 'exec 1>&3; [ -f /tmp/current ] && mv /tmp/current /tmp/last; exec > >(tee /tmp/current)' DEBUG"""
        pyautogui.write(save_output_script, interval=0.1)
        pyautogui.press("enter")
        time.sleep(1)
    else:
        print("Captura de saída já configurada. Pulando essa etapa.")

    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    
    pyautogui.write(curl_command, interval=0.15)
    pyautogui.press("enter")
    print("Comando cURL executado.")

    time.sleep(6)

    # 🔍 Espera ativa para garantir que o arquivo /tmp/last esteja preenchido
    retry_count = 0
    max_retries = 5
    response_from_file = ""

    while retry_count < max_retries:
        if os.path.exists("/tmp/last") and os.path.getsize("/tmp/last") > 0:
            with open("/tmp/last", "r") as file:
                response_from_file = file.read().strip()
            if response_from_file:
                break  # Sai do loop assim que encontrar conteúdo
        print(f"Tentativa {retry_count + 1}: Arquivo /tmp/last ainda vazio, aguardando...")
        time.sleep(2)
        retry_count += 1

    print(f"Resposta capturada: {response_from_file}")

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

    os.system("pkill xterm")

