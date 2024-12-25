l1=float(input('Qual o cumprimento do lado 1 triângulo'))
l2=float(input('Qual o cumprimento do lado 2 triângulo'))
l3=float(input('Qual o cumprimento do lado 3 triângulo'))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('Os valores formam um triangulo')
else:
    print('Os valores não formam trinangulo')