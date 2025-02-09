import random
def hangman(word):
	wrong = 0
	lista_letras = []
	for letra in word:
		lista_letras.append(letra)
	board = ['_'] * len(lista_letras)
	while True:
		print(''.join(board))
		letra = input('digite uma letra')
		if letra in lista_letras:
			print('boa!')
			index = lista_letras.index(letra)
			board [index] = letra
			lista_letras [index] = '$'
		else:
			print('o boneco toma forma...')
			wrong+= 1
		if wrong == len(lista_letras):
			print('enforcado')
			print('a palavra era: ', word)
			break
		if not '_' in board:
			print(''.join(board))
			print('o boneco vive!')
			break
with open('palavras forca.txt', 'r') as arquivo:
	palavras = arquivo.readlines()
for index, palavra in enumerate(palavras):
	palavras [index] = palavras [index].replace('\n', '')
hangman(palavras [random.randint(0, len(palavras))])
input('saia')
