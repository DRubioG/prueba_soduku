import cv2
import numpy as np

def localizador_numero(imgR, thres=240, resizeH=300, resizeW=300, areaMin=200, areaMax=2000, marginW=4, marginH=4, valmedia=254.9):  
  """
  localizador_numero:
    Input:
      imgR: imagen de entrada
      thres: valor del threshold de entrada
      resizeH/resizeW: valor de reescalado en ancho y/o alto
      areaMin/areaMax: area mínima/máxima para detectar casillas
      marginW/marginH: margen para evitar los bordes internos de las casillas, tanto horizontal como vertical
      valmedia: valor desde el que se considera que la casilla contiene un número
    Ouput:
      areas: lista de areas que se consideran casillas
      numero: lista de casillas con números
  """
  img=cv2.resize(imgR, (resizeH,resizeW), interpolation=cv2.INTER_LINEAR) #reescalo la imagen a 300x300

  ret, imgthres=cv2.threshold(img, thres, 255, cv2.THRESH_BINARY) #aplico el threshold

  cv2.rectangle(imgthres, (1,1), (resizeW-1, resizeH-1), (255, 255, 255), 3) # elimino el contorno que rodea a la imagen
  contours,hierarchy =cv2.findContours(imgthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #extraigo los contornos de la imagen del sudoku
  img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
  areas=[]
  numero=[]

  for con in contours:
      area=cv2.contourArea(con) #calculamos el area de cada contorno
      if (area > areaMin) & (area< areaMax):
          x, y, h, w=cv2.boundingRect(con) #si el area del contorno esta entre 200 y 2000 calculamos cual es rectangulo que contiene el contorno
          cv2.rectangle(img, (x+4,y+4), (x+w-4, y+h-4), (255, 255, 0), 1) #lo pintamos
          areas.append(con) #añadimos el contorno a la lista de areas
          pru=imgthres[y+marginH:y+h-marginH, x+marginW:x+w-marginW] #extraemos del la imagen threshold el contorno que contiene el area
          media=cv2.mean(pru)[0] #calculamos la media de los pixeles de la imagen
          if  media < valmedia:
            numero.append(con)
            cv2.rectangle(img, (x+marginH,y+marginH), (x+w-marginW, y+h-marginW), (255, 0, 255), 1)
  return areas, numero

imgR=cv2.imread('imagenes/test.png', 0)
localizador_numero(imgR)
#cv2.imshow("img", img)
cv2.waitKey(0)
