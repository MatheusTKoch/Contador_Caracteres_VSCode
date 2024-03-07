import keyboard
import time
import pyautogui
import sqlite3

class TypingTracker:
    def __init__(self):
        self.start_time = time.time()
        self.total_characters = 0

    def track_typing(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            self.total_characters += 1

    def start_tracking(self):
        keyboard.hook(self.track_typing)

    def stop_tracking(self):
        keyboard.unhook_all()

    def get_elapsed_time(self):
        return time.time() - self.start_time

    def get_total_characters(self):
        return self.total_characters
    
    def initialize_database():
        connection = sqlite3.connect('typing_stats.db')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS typing_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                elapsed_time REAL,
                total_characters INTEGER
            )
        ''')
        connection.commit()
        connection.close()

def is_vscode_active():
    active_window_title = pyautogui.getActiveWindowTitle()
    return "Visual Studio Code" in active_window_title

if __name__ == "__main__":
    tracker = TypingTracker()
    tracker.start_tracking()

    try:
        while True:
            if is_vscode_active():
                time.sleep(1)
                elapsed_time = tracker.get_elapsed_time()
                total_characters = tracker.get_total_characters()
                print(f"Tempo total: {elapsed_time:.2f} segundos, Caracteres totais: {total_characters}")
    except KeyboardInterrupt:
        tracker.stop_tracking()


        valor1 = int(input("Digite o primeiro valor:"))
        valor2 = int(input("Digite o segundo valor:"))
        divisao = valor1 / valor2
        print("Resultado da divisao", divisao)
