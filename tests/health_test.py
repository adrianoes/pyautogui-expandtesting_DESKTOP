import time
import pyautogui

def test_open_and_maximize_xterm():
    # Abre o terminal xterm
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(2)  # Espera o terminal abrir

    # Maximiza a janela do terminal
    pyautogui.hotkey("ctrl", "alt", "shift", "f")  # Maximiza a janela no xterm
    time.sleep(2)

    # Verifica se a janela do terminal foi aberta
    screen = pyautogui.screenshot()
    terminal_found = pyautogui.locateOnScreen('terminal_icon.png')  # Verifica se o ícone do terminal está visível

    if terminal_found:
        print("Terminal encontrado na tela.")
    else:
        print("Terminal não encontrado na tela.")

    # Verificar se a janela foi maximizada, aqui apenas simulando um simples check
    # Verificando se o terminal ocupa uma área grande da tela
    screen_width, screen_height = pyautogui.size()
    terminal_position = pyautogui.getWindowsWithTitle("xterm")

    if terminal_position and terminal_position[0].width == screen_width and terminal_position[0].height == screen_height:
        print("A janela do terminal foi maximizada.")
    else:
        print("A janela do terminal não foi maximizada.")

    # Aguarda mais alguns segundos para a visualização
    time.sleep(5)

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")
