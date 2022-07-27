#Funções

import os

#Devido a mudança de comando no cmd do windows e no terminal do linux
#Adaptei o comando para o cmd e terminal
if os.name == 'nt':
	limpar = 'cls'
else:
	limpar = 'clear'

#Tabela de cores
ciano = '\033[1;36m'
reset = '\033[0;00m'
vermelho = 	'\033[1;91m'
verde = '\033[1;92m'
magenta = '\033[1;35m'
cyan = 	'\033[1;96m'
Azul = '\033[1;94m'
vermelho_fundo = '\033[1;41m'

#Desenha titulo e forca
def forcas (erros):
    if erros == 0:
        forca()
    elif erros == 1:
        erro1()
    elif erros == 2:
        erro2()
    elif erros == 3:
        erro3()
    elif erros == 4:
        erro4()
    elif erros == 5:
        erro5()

def titulo():
    print(cyan + '''
 _ ____ ____ ____    ___  ____    ____ ____ ____ ____ ____ 
 | |  | | __ |  |    |  \ |__|    |___ |  | |__/ |    |__| 
_| |__| |__] |__|    |__/ |  |    |    |__| |  \ |___ |  | 
                                                        
    
    ''' + reset)

def forca():
    print('''

    ___________
    |         |
    |
    |
    |
____|____
    ''')

def erro1():
    print('''
    ___________
    |         |
    |        ( )
    |
    |
____|____
        ''')

def erro2():
    print('''

    ___________
    |         |
    |        ( )
    |         |
    |         |
____|____
        ''')

def erro3():
    print('''

    ___________
    |         |
    |        ( )
    |         |\ 
    |         |
____|____
        ''')

def erro4():
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____
        ''')

def erro5():
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____      \ 
        ''')

def erro6():
    os.system(limpar)
    print( ''' 

    ___________  
    |         |  
    |        \U0001F635 
    |        /|\ 
    |         |
____|____    / \ Você perdeu! 
        ''')

def vitoria():
    os.system(limpar)
    titulo()
    print('''
    \U0001F929 
   \ | /
     |
    / \ 
        Você venceu, parabéns!!! 
    ''')

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']