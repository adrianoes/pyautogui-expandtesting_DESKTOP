import time
import pyautogui
import json
import re
import pyperclip

def test_curl_response():
    # Abre o terminal no Ubuntu
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(2)  # Espera o terminal abrir

    # Digita o comando no terminal e executa
    command = "curl -X GET 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    pyautogui.write(command)
    pyautogui.press("enter")

    # Aguarda tempo suficiente para a resposta aparecer
    time.sleep(5)

    # Copia a resposta do terminal
    pyautogui.hotkey("ctrl", "shift", "c")
    time.sleep(2)

    # Obtém a resposta copiada
    response = pyperclip.paste()

    # Debug: Exibe a resposta copiada
    print("Curl response copied from terminal:")
    print(response)

    # Expressão regular para capturar o JSON
    json_match = re.search(r'({.*})', response, re.DOTALL)
    json_response = json_match.group(0) if json_match else "{}"

    # Armazenando os dados da resposta em uma variável (dicionário)
    data = json.loads(json_response)

    # Fazendo as asserções diretamente na variável
    assert data.get("success") == True
    assert data.get("status") == 200
    assert data.get("message") == "Notes API is Running"

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")
