n1=float(input('Nota da primeira avaliação'))
n2=float(input('Nota da segunda avaliação'))
m=(n1+n2)/2
print(f'A média do aluno foi {m}')
if m>=7:
    print('Aluno APROVADO!')
elif 7>=m>=5:
    print('Aluno de RECUPERAÇÃO!')
elif m<5:
    print('Aluno REPROVADO!')
