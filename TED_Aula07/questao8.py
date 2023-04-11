x = input('digite uma palavra: ')
w = ''
for i in x:
    w = i + w
if(x == w):
    print('Sim, é um palíndromo a palavra:', x)
else:
    print('Não é um palíndromo a palavra:', x)