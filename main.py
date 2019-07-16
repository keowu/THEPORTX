# -*- coding: utf-8 -*-
# DESENVOLVIDO POR @KEOWU
# THEPORTX - É UM SOFTWARE LIVRE
# USE E ABUSE COM MODERAÇÃO
# V 1.1 
#
import portscan
import listports
import os
import time


class ThePortX:
    def Sendportscan(self):
        protscann = portscan.comecaExecuta();
        executar = protscann.start();

    def Listportscan(self):
        listaportas = listports.Serial();
        executalist = listaportas.getSeriais();
        

class Creditos:
    def criador(self):
         print (a);
         print ("Uma ferramenta python de código aberto que auxilia o envio atráves de portas seriais !")
         print ("Desenvolvido por @keowu")
         print ("www.github.com/keowu")
         print ("Follow me on github :D")
         print ("Thanks for use !")
         time.sleep(6)
        
while (True):
    try:
        a = """
_________          _______  _______  _______  _______ _________         
\__   __/|\     /|(  ____ \(  ____ )(  ___  )(  ____ )\__   __/|\     /|
   ) (   | )   ( || (    \/| (    )|| (   ) || (    )|   ) (   ( \   / )
   | |   | (___) || (__    | (____)|| |   | || (____)|   | |    \ (_) / 
   | |   |  ___  ||  __)   |  _____)| |   | ||     __)   | |     ) _ (  
   | |   | (   ) || (      | (      | |   | || (\ (      | |    / ( ) \ 
   | |   | )   ( || (____/\| )      | (___) || ) \ \__   | |   ( /   \ )
   )_(   |/     \|(_______/|/       (_______)|/   \__/   )_(   |/     \|
            """
        print (a);
        print ("For stop press ctrl + z")
        print ("Execute using sudo python main.py for send DATA via serial !")
        print ("1 « SEND DATA VIA SERIAL PORT")
        print ("2 « LIST ALL DEVICES AND PORTS AVALIABLE")
        print ("3 « CRÉDITOS")
        escolha = input("Qual serviço lhe é útil ?")
        enviarserial = ThePortX();
        creditos = Creditos();
        if (escolha ==1):
             enviarserial.Sendportscan();
             break;
        elif (escolha ==2):
            enviarserial.Listportscan();
            break;
        elif (escolha ==3):
            creditos.criador();
        else:
             print ("Não existe essa opção !")
    except:
        print "Ocorreu um erro ao processar sua solicitação"