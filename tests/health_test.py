import time
import pyautogui
import os
import json

def test_xterm_curl():
    os.environ["DISPLAY"] = ":99"  # Usa o display virtual do Xvfb

    # Verifica se o terminal já está aberto
    existing_process = os.popen("pgrep xterm").read().strip()
    
    if not existing_process:
        print("Abrindo novo terminal xterm...")
        os.system("xterm &")  
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
        save_output_script = """exec 3>&1; trap 'exec 1>&3; [ -f /tmp/current ] && mv /tmp/current /tmp/last; exec > >(tee /tmp/current)' DEBUG"""
        pyautogui.write(save_output_script, interval=0.1)
        pyautogui.press("enter")
        time.sleep(1)
    else:
        print("Captura de saída já configurada. Pulando essa etapa.")

    # Comando cURL
    curl_command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    
    # Escreve e executa o comando
    pyautogui.write(curl_command, interval=0.15)  
    pyautogui.press("enter")  
    print("Comando cURL executado.")

    # Espera a resposta ser salva no arquivo
    time.sleep(6)  

    # Lê o conteúdo do arquivo /tmp/last onde o output do último comando foi salvo
    response_from_file = ""
    if os.path.exists("/tmp/last"):
        with open("/tmp/last", "r") as file:
            response_from_file = file.read().strip()

    # Exibe a resposta capturada
    print(f"Resposta capturada: {response_from_file}")

    # **Fecha o terminal após capturar a resposta**
    os.system("pkill xterm")

    # Converte a resposta para JSON
    try:
        response_json = json.loads(response_from_file)
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
