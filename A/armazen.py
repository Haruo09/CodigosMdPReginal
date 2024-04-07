armazen = {}

while True:
    # Entrada
    entrada = input()
    if entrada == "0":
        break
    else:
        C, A, L = entrada.split()
    
    # Processamento
    if A == "adicionar":
        armazen[C] = L
    else:
        armazen[C] = "nao encontrado"
    

# Saída
for k, v in armazen.items():
    print(k, v)
