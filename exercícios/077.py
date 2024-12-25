t='paralelo','claro','pote','fisica','papel','pedra','carta','pino'
for c in t:
    print(c, end='        ')
    for l in c:
        if l in 'aeiou':
            print(l, end='')
