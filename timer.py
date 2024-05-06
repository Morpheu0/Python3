import tkinter as tk
import datetime
import time

def update_clock():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    label.config(text=formatted_time)
    label.after(1000, update_clock)  # Atualiza o relógio a cada segundo

# Configuração da janela
window = tk.Tk()
window.title("Relógio em Python")

# Label para exibir o horário
label = tk.Label(window, font=("Arial", 50), bg="white")
label.pack(padx=20, pady=20)

# Atualiza o relógio pela primeira vez
update_clock()

# Inicia a aplicação
window.mainloop()
