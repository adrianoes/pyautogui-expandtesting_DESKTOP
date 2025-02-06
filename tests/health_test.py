import time
import pyautogui
import pyperclip
import json
import os
import re

def test_curl_response():
    # Abre o terminal no Ubuntu
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(10)  # Espera o terminal abrir

    # Digita o comando no terminal e executa
    command = "curl -X GET 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json'"
    pyautogui.write(command)
    pyautogui.press("enter")

    # Aguarda tempo suficiente para resposta aparecer
    time.sleep(10)    

    # Copia a resposta do terminal
    pyautogui.hotkey("ctrl", "shift", "c")
    time.sleep(10)

    # Obtém a resposta copiada
    response = pyperclip.paste()

    # Debug: Exibe a resposta copiada
    print("Curl response copied from terminal:")
    print(response)

    # Expressão regular para capturar o JSON
    json_match = re.search(r'({.*})', response, re.DOTALL)
    json_response = json_match.group(0) if json_match else "{}"

    # Salva o JSON no arquivo
    resources_dir = "resources"
    os.makedirs(resources_dir, exist_ok=True)
    json_path = os.path.join(resources_dir, "testdata.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(json.loads(json_response), json_file, indent=4)

    # Lê o JSON salvo e faz asserções
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    assert data.get("success") == True
    assert data.get("status") == 200
    assert data.get("message") == "Notes API is Running"

    # Remove o arquivo JSON após o teste
    os.remove(json_path)

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")
