txt = str(input("Digite algo: "))
print("A letra 'A' apareceu {} vezes no texto inserido".format(txt.upper().count('A')))
print(txt.upper().find("A")+1)
print(txt.upper().rfind("A")+1)
