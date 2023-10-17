import random
palavras = ['carros', 'caneta', 'estante', 'livros', 'gato']
sorteado = random.choice(palavras)
print(sorteado)
tentativa = 0

print('=' * 40)
print(f'{"JOGO DA FORCA":^40}')
print('=' * 40)

print('|-------|\n'
      '|       |\n'
      '|\n'
      '|\n'
      '|\n'
      '|')

letra = input('Digite uma letra: ')
for l in range(len(sorteado) -1):
    if letra in sorteado:
        print('Você  acertou uma letra!')
        letra = input('Digite uma letra: ')
    while letra not in sorteado:
        tentativa += 1
        if tentativa == 1:
            print('|-------|\n'
                  '|       |\n'
                  '|     (^.^)\n'
                  '|\n'
                  '|\n'
                  '|')
            letra = input('Você errou uma letra! Tente novamente: ')
        elif tentativa == 2:
            print('|-------|\n'
                  '|       |\n'
                  '|     (^.^)\n'
                  '|       |\n'
                  '|\n'
                  '|')
            letra = input('Você errou uma letra! Tente novamente: ')
        elif tentativa == 3:
            print('|-------|\n'
                  '|       |\n'
                  '|     (^.^)\n'
                  '|      /|\n'
                  '|\n'
                  '|')
            letra = input('Você errou uma letra! Tente novamente: ')
        elif tentativa == 4:
            print('|-------|\n'
                  '|       |\n'
                  '|     (^.^)\n'
                  '|      /|\ \n'
                  '|\n'
                  '|')
            letra = input('Você errou uma letra! Tente novamente: ')
        elif tentativa == 5:
            print('|-------|\n'
                  '|       |\n'
                  '|     (^.^)\n'
                  '|      /|\ \n'
                  '|      /\n'
                  '|')
            letra = input('Você errou uma letra! Tente novamente: ')
        elif tentativa == 6:
            print('|-------|\n'
                  '|       |\n'
                  '|     (^.^)\n'
                  '|      /|\ \n'
                  '|      / \ \n'
                  '|')
        else:
            break
if tentativa >= 5:
    print('INFELIZMENTE VOCÊ PERDEU!')
else:
    print('PARABÉNS, VOCÊ VENCEU!')