f=str(input('Digite algo')).strip().lower()
print(f'Seu nome possue a letra A? {'a' in f}\nA letra A aparece {f.count('a')} vezes.')
print(f'A letra a aparece na posição {f.find('a')+1} primeiro e na posição {f.rfind('a')+1} por ultimo.')
