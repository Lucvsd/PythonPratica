# Número Tipo numérico
# 5 [ ] inteiro [ ] ponto flutuante
# 5.0 [ ] inteiro [ ] ponto flutuante
# 4.3 [ ] inteiro [ ] ponto flutuante
# -2 [ ] inteiro [ ] ponto flutuante
# 100 [ ] inteiro [ ] ponto flutuante
# 1.333 [ ] inteiro [ ] ponto flutuante

# Lista de números
numeros = [5, 5.0, 4.3, -2, 100, 1.333]

# Percorre a lista e verifica o tipo
for numero in numeros:
    if isinstance(numero, int):
        print(f"{numero} é inteiro")
    elif isinstance(numero, float):
        print(f"{numero} é ponto flutuante")