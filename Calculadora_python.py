import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacao = operacao_var.get()

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não é permitida!")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Erro", "Selecione uma operação válida")
            return
        
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x300")

# Campos de entrada
entrada_num1 = tk.Entry(janela)
entrada_num1.pack(pady=5)

entrada_num2 = tk.Entry(janela)
entrada_num2.pack(pady=5)

# Opções de operação
operacao_var = tk.StringVar(value="+")
operacoes = ["+", "-", "*", "/"]
for op in operacoes:
    tk.Radiobutton(janela, text=op, variable=operacao_var, value=op).pack()

# Botão de calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack(pady=10)

# Exibir resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack(pady=10)

# Rodar a interface
tk.mainloop()


