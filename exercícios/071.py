valor=int(input('Qual será o valor sacado?'))
valorr=0
n50=0
n20=0
n10=0
n1=0
while valorr!=valor:
    if valor%50>=0:
        qn=valor//50
        n50+=qn
        valorr+=50*qn
    else:
        if valor%20>=0:
            qn=valor//20
            n20+=qn
            valorr += 20 * qn
print(n50, n20)