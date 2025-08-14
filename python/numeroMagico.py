numeroMagico = 47
tentativas = 0

while tentativas < 3:
  numero = input('Adivinhe o número mágico: ')

  if int(numero) == numeroMagico:
    print('Sabe muito')
    break
  tentativas += 1
else:
  print('cabeção')