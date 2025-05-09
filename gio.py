# programa múmero crescente
n1= int(input('número 1:'))
n2= int(input('número 2:'))
n3= int(input('número 3:'))
if n1 <= n2 <= n3:
   menor, meio, maior = n1, n2, n3
elif n1 <= n3 <= n2:
   menor, meio, maior = n1, n3, n2
elif n2 <= n1 <= n3:
   menor, meio, maior = n2, n1, n3
elif n2 <= n3 <= n1:
   menor, meio, maior = n2, n3, n1
elif n3 <= n1 <= n2:
   menor, meio, maior = n3, n1, n2
else:
   menor, meio, maior = n3, n2, n1
   print('ordem crescente dos números:', menor, meio, maior)


# programa tabuada
n = int(input('número:'))
for i in range(1,11):
    print (f'{n} X {i} = {n * i}')
