import subprocess
import time
import pyautogui
import pyperclip
import json
import os
import re

# Test case function for pytest
def test_curl_response():
    # Abrir o terminal bash diretamente
    subprocess.Popen(["bash", "-c", "echo 'Terminal Bash aberto'"])  # Inicia o bash com um comando simples

    time.sleep(5)  # Esperar o terminal abrir

    # Maximize the terminal window by sending Alt + Space, then X
    pyautogui.hotkey("alt", "space")  # Abre o menu de controle da janela
    time.sleep(0.5)
    pyautogui.press("x")  # Maximiza a janela
    time.sleep(1)  # Aguarda o tempo necessário para maximizar

    # Digitar o comando curl e pressionar Enter
    command = "curl -X 'GET' 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    pyperclip.copy(command)  # Copia o comando para a área de transferência
    time.sleep(1)
    # Usar pyautogui para colar e executar o comando no terminal
    pyautogui.hotkey("ctrl", "v")  # Cola o comando
    pyautogui.press("enter")  # Executa o comando

    # Espera pela resposta do comando
    time.sleep(10)

    # Seleciona e copia a resposta do terminal
    pyautogui.hotkey("ctrl", "shift", "a")  # Seleciona todo o texto
    time.sleep(2)  # Garantir que a seleção foi feita
    pyautogui.hotkey("ctrl", "c")  # Copia a seleção
    time.sleep(2)  # Garantir que a cópia foi concluída

    # Recupera o texto copiado
    copied_text = pyperclip.paste()

    # Depuração: imprime o texto copiado para verificar
    print("Texto copiado do terminal:")
    print(copied_text)

    # Expressão regular para encontrar um JSON válido no texto copiado
    json_match = re.search(r'({.*})', copied_text, re.DOTALL)

    if json_match:
        json_response = json_match.group(0)  # Extrai o JSON
    else:
        json_response = "{}"  # Caso não encontre um JSON, define um JSON vazio

    # Certifique-se de que o diretório 'resources' existe
    resources_dir = "resources"
    os.makedirs(resources_dir, exist_ok=True)

    # Salva a resposta JSON no arquivo testdata.json
    json_path = os.path.join(resources_dir, "testdata.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(json.loads(json_response), json_file, indent=4)

    # Lê o arquivo JSON e extrai variáveis
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    success = data.get("success")
    status = data.get("status")
    message = data.get("message")

    # Realiza asserções para validar a resposta
    assert success == True, f"Expected success=True but got {success}"
    assert status == 200, f"Expected status=200 but got {status}"
    assert message == "Notes API is Running", f"Expected message='Notes API is Running' but got {message}"

    # Apaga o arquivo testdata.json após o teste
    if os.path.exists(json_path):
        os.remove(json_path)
        print(f"File {json_path} has been deleted.")
    
    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")  # Envia Alt+F4 para fechar a janela
