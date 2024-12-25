t= (int(input('Digite um valor')),
int(input('Digite um valor')),
int(input('Digite um valor')),
int(input('Digite um valor')))
print(t.count(9))
print(t.index(3)+1)
for c in t:
    if c%2==0:
        print (c, end=' ')
