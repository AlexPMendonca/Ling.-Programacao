#4) Implementar uma função que retorne verdadeiro se o número for primo
#(falso caso contrário). Testar de 1 a 100.

def is_primo(n):
    """Retorna True se n for primo, False caso contrário."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Testa os números de 1 a 100
for num in range(1, 101):
    if is_primo(num):
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")
