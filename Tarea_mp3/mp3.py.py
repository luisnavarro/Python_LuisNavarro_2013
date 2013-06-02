
#Luis Antonio Navarro Canales
#Codigo: SMIS137611

import os
import sys
import pygame.mixer
import pygame.cdrom

pygame.mixer.init(44100, -16, 2, 4096)
reload(sys)
sys.setdefaultencoding('utf8')

#Para poder reproducir un archivo .mp3 ubicado en otra carpeta colocamos "\"
#direccionamos la ubicacion del archivo
pygame.mixer.music.load('C:\Users\Luis\Documents\GitHub\Python_LuisNavarro_2013\mp3_stored\Niggas_in_Paris.mp3')
pygame.mixer.music.play()

#Volumen must be set between 0 to 1
#Indicaciones: Ejecutar cada linea de codigo en el shell. Quitar el '#' 

#pygame.mixer.music.set_volume(0.5) 
#pygame.mixer.music.set_volume(0.2)
#pygame.mixer.music.set_volume(1.0)
#pygame.mixer.music.stop()
