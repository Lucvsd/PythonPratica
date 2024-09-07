"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

tabuada = int(input("Tabuada do numero: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

# Verificação fora do loop
if inicio > fim:
    print("O primeiro valor não pode ser maior que o segundo valor.")
else:
    for cont in range(inicio, fim + 1):
        print("%d x %d = %d" % (tabuada, cont, tabuada * cont))
