n = int(input("Digite quantos valores vao ser ordenados: "))
vet=[]
print("Digite os valores:")
for i in range(n):
    valor = int(input(f"Valor {i+1}: "))
    vet.append(valor)
for i in range (n):
    for j in range(n-1):
        if vet[j] > vet[j+1]:
            temp = vet[j]
            vet[j] = vet[j+1]
            vet[j+1] = temp
print("Valores ordenados: ")
for valor in vet:
    print(valor)
