import tkinter as tk
from tkinter import messagebox

# Variável global para armazenar o código de barras válido
codigo_valido = "7896676431674"  # Exemplo de código válido definido manualmente

def validar_codigo_barras():
    codigo = entry_codigo.get().strip()
    
    # Verifica se o código inserido corresponde ao código válido
    if codigo == codigo_valido:
        messagebox.showinfo("Validação", "✅ Código de barras válido!")
    else:
        messagebox.showerror("Validação", "❌ Código de barras inválido!")
    
    # Limpar o campo após validação
    entry_codigo.delete(0, tk.END)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Validador de Códigos de Barras EAN-13")
root.geometry("400x200")

# Widgets da interface
label_titulo = tk.Label(root, text="Validador de Códigos de Barras EAN-13", font=("Helvetica", 14, "bold"))
label_titulo.pack(pady=10)

label_codigo = tk.Label(root, text="Digite o código de barras:")
label_codigo.pack()

entry_codigo = tk.Entry(root, font=("Helvetica", 12))
entry_codigo.pack(pady=5)

btn_validar = tk.Button(root, text="Validar Código", command=validar_codigo_barras, font=("Helvetica", 12), bg="lightblue")
btn_validar.pack(pady=10)

# Inicia a interface
root.mainloop()
