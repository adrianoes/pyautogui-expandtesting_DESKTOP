import time
import pyautogui
import json
import os

def test_curl_response():
    # Abre o terminal no Ubuntu
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(2)  # Espera o terminal abrir

    # Define caminho para salvar a resposta
    json_path = os.path.expanduser("~/curl_response.json")

    # Digita o comando no terminal e redireciona para um arquivo
    command = f"curl -X GET 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json' > {json_path}"
    pyautogui.write(command)
    pyautogui.press("enter")

    # Aguarda o curl processar e salvar a resposta
    time.sleep(5)    

    # Lê o JSON salvo no arquivo
    with open(json_path, "r", encoding="utf-8") as json_file:
        response = json_file.read()

    print("Curl response from file:")
    print(response)

    # Converte string JSON para dicionário
    data = json.loads(response)

    # Faz as asserções
    assert data.get("success") == True
    assert data.get("status") == 200
    assert data.get("message") == "Notes API is Running"

    # Remove o arquivo JSON após o teste
    os.remove(json_path)

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")
