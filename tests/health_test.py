import time
import pyautogui
import json
import os

def test_curl_response():
    # Abre o terminal no Ubuntu
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(2)  # Espera o terminal abrir

    # Define o diretório "resources" e o caminho para o arquivo JSON
    resources_dir = os.path.join(os.getcwd(), "resources")
    os.makedirs(resources_dir, exist_ok=True)  # Garante que o diretório "resources" exista

    json_path = os.path.join(resources_dir, "curl_response.json")  # Caminho para salvar o JSON

    # Digita o comando no terminal e redireciona para um arquivo
    command = f"curl -X GET 'https://practice.expandtesting.com/notes/api/health-check' -H 'accept: application/json' > {json_path}"
    pyautogui.write(command)
    pyautogui.press("enter")

    # Aguarda o curl processar e salvar a resposta
    time.sleep(5)    

    # Lê o JSON salvo no arquivo
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            response = json_file.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {json_path}")
        raise  # Reraise the exception to stop the test

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
