import time
import pyautogui
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
    time.sleep(20)

    # Copia a resposta do terminal
    pyautogui.hotkey("ctrl", "shift", "c")
    time.sleep(2)

    # Obtém a resposta copiada
    response = pyperclip.paste()

    # Debug: Exibe a resposta copiada
    print("Curl response copied from terminal:")
    print(response)

    # # Expressão regular para capturar o JSON
    # json_match = re.search(r'({.*})', response, re.DOTALL)
    # if not json_match:
    #     print("Erro: Não foi possível encontrar um JSON válido na resposta.")
    #     return

    # json_response = json_match.group(0)
    # print("JSON capturado:", json_response)

    # # Armazenando os dados da resposta em uma variável (dicionário)
    # try:
    #     data = json.loads(json_response)
    # except json.JSONDecodeError as e:
    #     print(f"Erro ao tentar decodificar o JSON: {e}")
    #     return

    # # Fazendo as asserções diretamente na variável
    # assert data.get("success") == True, f"Esperado 'success' como True, mas recebeu {data.get('success')}"
    # assert data.get("status") == 200, f"Esperado 'status' como 200, mas recebeu {data.get('status')}"
    # assert data.get("message") == "Notes API is Running", f"Esperado 'message' como 'Notes API is Running', mas recebeu {data.get('message')}"

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")
