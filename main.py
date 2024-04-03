import tkinter as tk
from datetime import datetime

class RelogioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio")
        self.label_hora = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.label_hora.pack(padx=20, pady=20)
        self.atualizar_hora()

    def atualizar_hora(self):
        hora_atual = datetime.now().strftime("%H:%M:%S")
        self.label_hora.config(text=hora_atual)
        self.root.after(1000, self.atualizar_hora)  # Atualiza a hora a cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    app = RelogioApp(root)
    root.mainloop()
