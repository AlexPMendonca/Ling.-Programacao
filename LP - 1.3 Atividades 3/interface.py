import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        # Captura o nome, endereco, peso e altura inseridos
        nome = entry_nome.get()
        endereco = entry_endereco.get()        
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # Verifica se os campos obrigatórios estão preenchidos
        if not nome:
            messagebox.showerror("Erro", "Por favor, insira o nome do paciente.")
            return
        
        if not endereco:
            messagebox.showerror("Erro", "Por favor, insira o endereço do paciente.")
            return

        # Calcula o IMC
        imc = peso / (altura ** 2)

        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 24.9:
            classificacao = "Peso normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        # Exibe o resultado na caixa de texto
        resultado = f"{nome}, seu IMC é: {imc:.2f}\nClassificação: {classificacao}"
        text_resultado.delete(1.0, tk.END)  # Limpa o conteúdo atual
        text_resultado.insert(tk.END, resultado)  # Insere o novo conteúdo
    
    except ValueError:
        # Exibe uma mensagem de erro se o valor não for válido
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

# Função para reiniciar os campos
def reiniciar_imc():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    text_resultado.delete(1.0, tk.END)  # Limpa a caixa de texto

# Função para sair da aplicação
def button_sair_imc():
    root.quit()

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("650x250")  # Tamanho da janela ajustado

# Labels e Entry para o nome
label_nome = tk.Label(root, text="Nome do paciente:")
label_nome.grid(row=0, column=0, sticky="w", padx=10, pady=5)

entry_nome = tk.Entry(root, width=40)######
entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Labels e Entry para o endereço
label_endereco = tk.Label(root, text="Endereço Completo:")
label_endereco.grid(row=1, column=0, sticky="w", padx=10, pady=5)

entry_endereco = tk.Entry(root,width=40)
entry_endereco.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Labels e Entry para o peso
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.grid(row=2, column=0, padx=10, pady=5,sticky="w")

entry_peso = tk.Entry(root)
entry_peso.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Labels e Entry para a altura
label_altura = tk.Label(root, text="Altura (m):")
label_altura.grid(row=3, column=0, sticky="w", padx=10, pady=5)

entry_altura = tk.Entry(root)
entry_altura.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Botões lado a lado na linha 4
button_calcular = tk.Button(root, text="Calcular", command=calcular_imc)
button_calcular.grid(row=4, column=0, padx=10, pady=10, sticky="w")

button_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar_imc)
button_reiniciar.grid(row=4, column=1, padx=10, pady=10, sticky="w")

button_sair = tk.Button(root, text="Sair", command=button_sair_imc)
button_sair.grid(row=4, column=2, padx=10, pady=10, sticky="w")

# Caixa de texto para exibir o resultado
text_resultado = tk.Text(root, height=3, width=25, wrap=tk.WORD)
text_resultado.grid(row=2, column=2, columnspan=3, padx=10, pady=10)

# Inicia o loop principal da interface
root.mainloop()
