import pygame, sys
from pygame.locals import *
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import csv
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import webbrowser

pygame.init()

PANTALLA = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RECETARIO")

#Fondo
fondo=pygame.image.load("images/menuFondo.jpg")
fondo = pygame.transform.scale(fondo,(1000,700))

fondoComida=pygame.image.load("images/menu2.jpg")
fondoComida = pygame.transform.scale(fondoComida,(1000,700))
fondoBebida=pygame.image.load("images/menu2.jpg")
fondoBebida = pygame.transform.scale(fondoBebida,(1000,700))

#Icono
icono=pygame.image.load("images/icono.jpg")
pygame.display.set_icon(icono)

#Imagen comida (Rectangulo)
ImaComida = pygame.image.load("images/Comida.png")
ImaComida = pygame.transform.scale(ImaComida, (200, 200))
rectComida = ImaComida.get_rect()
rectComida.center = (250, 400)
#Imagen bebida (Rectangulo)
ImaBeida = pygame.image.load("images/Bebidas.png")
ImaBeida = pygame.transform.scale(ImaBeida, (200, 200))
rectBebida = ImaBeida.get_rect()
rectBebida.center = (750, 400)


#Imagen Licuado de Fresa (Rectangulo)
ImaLicuado = pygame.image.load("images/LicuadoFresa.png")
ImaLicuado = pygame.transform.scale(ImaLicuado, (200, 200))
rectLicuado = ImaLicuado.get_rect()
rectLicuado.center = (300, 350)
#Imagen Jugo verde (Rectangulo)
ImaJugo = pygame.image.load("images/JugoVerde.png")
ImaJugo = pygame.transform.scale(ImaJugo, (200, 200))
rectJugo = ImaJugo.get_rect()
rectJugo.center = (700, 350)
#Imagen Jugo de naranja (Rectangulo)
ImaNaranja = pygame.image.load("images/JugoNaranja.png")
ImaNaranja = pygame.transform.scale(ImaNaranja, (200, 200))
rectNaranja = ImaNaranja.get_rect()
rectNaranja.center = (500, 600)


#Imagen Arroz frito (Rectangulo)
ImaArroz = pygame.image.load("images/ArrozFrito.png")
ImaArroz = pygame.transform.scale(ImaArroz, (150, 150))
rectArroz = ImaArroz.get_rect()
rectArroz.center = (200, 350)
#Imagen Chilaquiles rojos (Rectangulo)
ImaChilaquiles = pygame.image.load("images/ChilaquilesRojos.png")
ImaChilaquiles = pygame.transform.scale(ImaChilaquiles, (150, 150))
rectChilaquiles = ImaChilaquiles.get_rect()
rectChilaquiles.center = (500, 350)
#Imagen Guacamole (Rectangulo)
ImaGuacamole = pygame.image.load("images/Guacamole.png")
ImaGuacamole = pygame.transform.scale(ImaGuacamole, (150, 150))
rectGuacamole = ImaGuacamole.get_rect()
rectGuacamole.center = (800, 350)
#Imagen Hot Cakes (Rectangulo)
ImaCakes = pygame.image.load("images/HotCakes.png")
ImaCakes = pygame.transform.scale(ImaCakes, (150, 150))
rectCakes = ImaCakes.get_rect()
rectCakes.center = (200, 580)
#Imagen Huevos a la mexicana (Rectangulo)
ImaHue = pygame.image.load("images/HuevoMexicana.png")
ImaHue = pygame.transform.scale(ImaHue, (150, 150))
rectHue = ImaHue.get_rect()
rectHue.center = (500, 580)
#Imagen Sopa de fideos (Rectangulo)
ImaFideo = pygame.image.load("images/SopaFideo.png")
ImaFideo = pygame.transform.scale(ImaFideo, (150, 150))
rectFideo = ImaFideo.get_rect()
rectFideo.center = (800, 580)


buttonComida = None
buttonBebida = None
buttonArroz = None
buttonChilaquiles = None
buttonGuacamole = None
buttonCakes = None
buttonHuev = None
buttonFideo = None
buttonLicuado = None
buttonJugo = None
buttonNaranja = None

principal = True
ventanaComida = None
ventanaBebida = None

def speak(text):
    voice = gTTS(text=text, lang="es", tld="com")
    filename = "voice.mp3"
    voice.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            position = pygame.mouse.get_pos()
            if buttonComida.collidepoint(position) and principal:
                principal=False
                ventanaComida = True
                print("Comida")
                PANTALLA.fill((0,0,0))
                PANTALLA.blit(fondoComida, (0, 0))
                buttonArroz = PANTALLA.blit(ImaArroz, rectArroz)
                buttonChilaquiles = PANTALLA.blit(ImaChilaquiles, rectChilaquiles)
                buttonGuacamole = PANTALLA.blit(ImaGuacamole, rectGuacamole)
                buttonCakes = PANTALLA.blit(ImaCakes, rectCakes)
                buttonHuev = PANTALLA.blit(ImaHue, rectHue)
                buttonFideo = PANTALLA.blit(ImaFideo, rectFideo)

            if not principal and ventanaComida:
                if buttonArroz.collidepoint(position):
                    file = open("ArrozFrito.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    file.close()
                elif buttonChilaquiles.collidepoint(position):
                    file = open("ChilaquilesRojos.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    file.close()
                elif buttonGuacamole.collidepoint(position):
                    file = open("Guacamole.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    file.close()
                elif buttonCakes.collidepoint(position):
                    file = open("HotCakes.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    file.close()
                elif buttonHuev.collidepoint(position):
                    file = open("HuevoMexicana.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    file.close()
                elif buttonFideo.collidepoint(position):
                    file = open("SopaFideo.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    file.close()


            if buttonBebida.collidepoint(position) and principal:
                principal = False
                ventanaBebida = True
                print("Bebida")
                PANTALLA.fill((0, 0, 0))
                PANTALLA.blit(fondoBebida, (0, 0))
                buttonLicuado = PANTALLA.blit(ImaLicuado, rectLicuado)
                buttonJugo = PANTALLA.blit(ImaJugo, rectJugo)
                buttonNaranja = PANTALLA.blit(ImaNaranja, rectNaranja)

            if not principal and ventanaBebida:
                if buttonLicuado.collidepoint(position):
                    file = open("LicuadoFresa.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    texto = " "
                    file.close()

                elif buttonNaranja.collidepoint(position):
                    file = open("JugoNaranja.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    texto = " "
                    file.close()

                elif buttonJugo.collidepoint(position):
                    file = open("JugoVerde.csv", newline='')
                    reader = csv.reader(file)
                    texto = ""
                    for l in list(reader):
                        if len(l) > 0:
                            "".join(l)
                            texto = texto + " " + l[0]
                    speak(texto)
                    texto = " "
                    file.close()


    if principal:
        PANTALLA.blit(fondo, (0, 0))
        buttonComida = PANTALLA.blit(ImaComida, rectComida)
        buttonBebida = PANTALLA.blit(ImaBeida, rectBebida)

    pygame.display.flip()