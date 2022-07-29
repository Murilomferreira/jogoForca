from random import randint
from temas import *
from funcoes import *
from time import sleep
import os


#Devido a mudança de comando no cmd do windows e no terminal do linux, adaptei o comando para o cmd e terminal
if os.name == 'nt':
	limpar = 'cls'
	reinicio = 'python game.py'
else:
	reinicio = 'python3 game.py'
	limpar = 'clear'

os.system(limpar)

#Escolher o tema para jogar
titulo()
print(f' [ 1 ] --> {vermelho}Objetos{reset} \n [ 2 ] --> {vermelho}Animais{reset} \n [ 3 ] --> {vermelho}Profissões{reset}')

try:
	tema = int (input('\n [tema]--> '))
except:
	print('erro')
	os.system(reinicio)

os.system(limpar)

#palavra é definida com base no tema
if tema == 1:
	num = randint(0, len(Objetos) -1)
	palavra = ' '.join(Objetos[num]).split()
elif tema == 2:
	num = randint(0, len(animais) -1)
	palavra = ' '.join(animais[num]).split()
elif tema == 3:
	num = randint(0, len(Profissões) -1)
	palavra = ' '.join(Profissões[num]).split()


num = len(palavra)


numletras = []
for c in range(num):
	numletras.append('_')


erros = 0

#Interface
titulo()
forca()


letras_usadas = []

#Game
while True:
	
	print(f'Letras descobertas {verde + " ".join(numletras) + reset}')
	print(f'letras erradas: {vermelho + " ".join(letras_usadas) + reset}')

	letra = input (f'[{verde}digite uma letra{reset}]-->  ')

	os.system(limpar)
	titulo()

	if letra not in char or letra in letras_usadas:
		forcas(erros)

	else:
		#Se a letra estiver presente na palavra	
		if letra in palavra:
			for i in range(len(palavra)):
				if palavra[i] == letra:
					numletras.pop(i)
					numletras.insert(i, letra)

			#As forcas são desenhadas com base na variável erros
			forcas(erros)

			#Caso a lista numletras seja igual a lista palavras, o usuário ganha
			if numletras == palavra:
				vitoria()
				print(f'A palavra era { verde + "".join(palavra)}')
				sleep(10)
				break

		#senao estiver
		else:
			erros = erros + 1
			letras_usadas.append(letra)
			#Desenha o personagem na forca quando o usuário erra
			forcas(erros)
			#se erros for igual a 6, o usuário perde
			if erros == 6:
				erro6()
				print(f'A palavra era {vermelho + "".join(palavra)}')	
				sleep(10)
				break
		
os.system(reinicio)