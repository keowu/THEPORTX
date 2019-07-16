# -*- coding: utf-8 -*-
import serial


porta = '/dev/ttyACM0'; #sua porta com padrão linux ou windows
baudrate = 9600; #baudrate de comunicação
interbyte = 2; #interbyte enviado


#use ttyUSB0 se for o caso, ou se for Windows, COMx.
#conectaserial = serial.Serial('/dev/ttyACM0',9600,timeout=2)
try:
    conectaserial = serial.Serial(porta,baudrate, timeout=interbyte)
except:
    #print("Não foi possivel conectar !")
    conectaserial = "não";