reta1 = int(input("Diigite o comprimento da reta: "))
reta2 = int(input("Diigite o comprimento da reta: "))
reta3 = int(input("Diigite o comprimento da reta: "))

if reta1<=0 or reta2<=0 or reta3<=0 :
   print("Lados nulos ou negativos nao sao aceitos.")

if reta1>=reta2+reta3 or reta2>=reta3+reta1 or reta3>=reta1+reta2 :
   print("Triangulo inexistente.")

if reta1==reta2 and reta2==reta3 :
   print("Triangulo equilatero.")

elif reta1==reta2 or reta2==reta3 or reta3==reta1 :
   print("Triangulo isosceles.")

else:
   print("Triangulo escaleno.")