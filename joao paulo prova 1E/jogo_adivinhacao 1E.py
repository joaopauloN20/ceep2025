import random 
# biblioteca para edificar o sorteio do numero, ja pronto, apenas iremos informar posteriormente o inter 

import os 
# biblioteca do sistema operacional, para limpar a tela, se windows cls, no linux clear
erro = 0
sorteado = random.randrange(0,100)
jogador =int(input("digite seu numero!:   "))
while(sorteado!=jogador):
    os.system("cls")
    if(sorteado>jogador):
        print("ERRO, o seu numero é maior")
    elif(sorteado<jogador):
        print("ERRO, seu numero é menor ")
        erros+=1
        jogador=int(input("digite seu numero:   "))
        print("numero" + str(jogador) + " ,voce certou em: " + str(erros+1) + "tentativas")