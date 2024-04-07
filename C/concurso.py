# entrada
p1, p2, p3, p4 = [float(x) for x in input().split()]

# processamento
print(p1, p2, p3, p4)
media = (p1 * 1 + p2 * 2 + p3 * 3 + p4 * 5)/11

# saída
print(f"{media:.2f}")
if media >= 6:
    print("classificado")
else:
    print("desclassificado")
