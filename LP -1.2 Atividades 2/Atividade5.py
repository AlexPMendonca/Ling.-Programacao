# 5) Escreva uma função que:
#a) Receba uma frase como parâmetro.
#b) Retorne uma nova frase com cada palavra com as letras invertidas.

def inverter_palavras(frase):
    # Divide a frase em palavras
    palavras = frase.split()

    # Inverte as letras de cada palavra
    palavras_invertidas = [palavra[::-1] for palavra in palavras]

    # Junta as palavras invertidas em uma nova frase
    nova_frase = ' '.join(palavras_invertidas)

    return nova_frase


# Exemplo de uso:
frase_original = "Linguagem de Programação"
nova_frase = inverter_palavras(frase_original)
print(nova_frase)
