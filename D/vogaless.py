vogais = "aeiouAEIOU"

palavra = input()
saida = ""

for char in palavra:
    if char not in vogais:
        saida += char

print(saida)
