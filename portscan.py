# -*- coding: utf-8 -*-
import config

conectaserial = config.conectaserial;

class Programa:
    def acontecePrograma(self):
        print "inciando conexao !"

class EnivoDados:
    def fazMagica(self):
            mandacomando = raw_input("Entre com o comando a ser enviado: ")
            conectaserial.write(mandacomando)
            print conectaserial.read_until('\n') 


class comecaExecuta:
    def start(self):
                    #pega os dados do arquivo config e salva em uma variável global
        if(config.conectaserial == "não"):
            print "Não possivel conectar" 
        else:   
            conectaserial = config.conectaserial;
            #inicia e instancia os objetos
            prog = Programa();
            prog.acontecePrograma();

            dados = EnivoDados();
            while (True):
                dados.fazMagica();