# prueba_soduku
 El objetivo de este repositorio es detectar las casillas de un sudoku que contienen un número

## Codigo
### Prueba 1
Esta prueba consiste en localizar cuales son las casillas que contienen un numero

""" python
imgR=cv2.imread('imagenes/test6.jpg', 0)
img=cv2.resize(imgR, (300,300), interpolation=cv2.INTER_LINEAR) #reescalo la imagen a 300x300
height, width = img.shape[:2] #extraigo la altura y la anchura de la imagen
ret, imgthres=cv2.threshold(img, thres, 255, cv2.THRESH_BINARY) #aplico el threshold
cv2.rectangle(imgthres, (1,1), (width-1, height-1), (255, 255, 255), 3) # elimino el contorno que rodea a la imagen
contours,hierarchy =cv2.findContours(imgthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #extraigo los contornos de la imagen del sudoku
"""
1. Primero se lee la imagen
![imagen](imagenes/test.png)
2. Se reescala para hacer más facil el trabajo
![imagen](imagenes/imagenes_prueba1/reescalado.jpg)
3. Se aplica un threshold para eliminar impurezas en la imagen
![imagen](imagenes/imagenes_prueba1/threshold.jpg)
4. Se superpone un rectangulo blanco son el sudoku para eliminar los margenes
5. Se obtienen los contornos de la imagen
![imagen](imagenes/imagenes_prueba1/contornos.jpg)
(Para poder ver las casillas se utiliza cambia la imagen original por una RGB)
"""python
img=cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
"""

