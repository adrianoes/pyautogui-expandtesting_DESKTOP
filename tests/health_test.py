import time
import pyautogui

def test_open_xterm():
    # Abre o terminal xterm maximizado
    pyautogui.hotkey("ctrl", "alt", "t")  # Atalho para abrir o terminal (com xterm configurado)
    time.sleep(5)  # Espera o terminal abrir

    # Maximiza a janela do terminal
    pyautogui.hotkey("ctrl", "alt", "shift", "f")  # Maximiza a janela no xterm (comando para maximizar no X11)
    time.sleep(5)

    # Aguarda alguns segundos para que possamos ver a janela maximizada
    print("Terminal aberto e maximizado.")
    time.sleep(5)

    # Fecha o terminal
    pyautogui.hotkey("alt", "f4")  # Fecha a janela do terminal
