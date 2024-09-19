def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testando a função com um exemplo
numero = int(input("Digite um número inteiro: "))
if is_prime(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
