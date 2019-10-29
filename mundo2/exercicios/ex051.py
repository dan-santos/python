primeiro = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

for i in range(1, 11):
    primeiro = primeiro + razao
    print(primeiro)
