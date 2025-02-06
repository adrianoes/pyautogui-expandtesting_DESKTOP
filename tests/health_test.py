import subprocess
import time
import pyautogui
import pyperclip
import json
import os
import re

# Test case function for pytest
def test_curl_response():
    # Executar o curl diretamente sem abrir um terminal gráfico
    command = ["curl", "-X", "GET", "https://practice.expandtesting.com/notes/api/health-check", "-H", "accept: application/json"]
    
    # Executar o comando curl e obter a resposta
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Se houver erro, imprima a mensagem de erro
    if stderr:
        print("Erro ao executar o comando curl:", stderr.decode())
    
    # Decodifique a resposta para texto
    response = stdout.decode()
    
    # Depuração: imprime a resposta do curl
    print("Resposta do curl:")
    print(response)
    
    # Expressão regular para encontrar um JSON válido no texto da resposta
    json_match = re.search(r'({.*})', response, re.DOTALL)

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
    
    # Aqui você ainda pode continuar com a automação gráfica, se necessário
    # Fecha o terminal ou qualquer outra interação que precise ser feita
    pyautogui.hotkey("alt", "f4")  # Envia Alt+F4 para fechar a janela
