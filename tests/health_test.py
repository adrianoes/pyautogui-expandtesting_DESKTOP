import time
import pyautogui
import os

def test_open_xterm():
    # Usar o xdotool para abrir o terminal
    os.system("xdotool key 'ctrl+alt+t'")  # Simula o atalho para abrir o terminal
    time.sleep(3)  # Espera o terminal abrir

    # Maximiza a janela do terminal
    pyautogui.hotkey("ctrl", "alt", "shift", "f")  # Maximiza a janela no xterm (comando para maximizar no X11)
    time.sleep(2)  # Aguarda a maximização

    # Captura a tela para ver se o terminal está visível
    screen = pyautogui.screenshot()
    screen.save("terminal_screenshot.png")  # Salva a captura da tela para verificação posterior

    # Aguarda alguns segundos para que possamos ver a janela maximizada
    print("Terminal aberto e maximizado.")
    time.sleep(5)

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")  # Fecha a janela do terminal
