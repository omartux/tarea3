# template matching utilizando la distancia euclidiana en 
# lugar de la multiplicacion punto a punto, 

import cv2 as cv
import numpy as np
import time # modulo para calculo de costo y complejidad

start_time = time.perf_counter ()

#creacion de ventana para el resultado final, esta definida en tama–o para que no 
#ocupe demasiada pantalla.
cv.namedWindow('Resultado', cv.WINDOW_NORMAL)
cv.resizeWindow('Resultado', 640,480)
# Lee la imagen de origen y la imagen del template:

img = cv.imread('imagen.png', 0)  # Lee la imagen para analizar  en escala de grises
template = cv.imread('template.png', 0)  # Lee la imagen del template en escala de grises

# Calcula las dimensiones de la imagen y el template:

img_height, img_width = img.shape
print(img_height)
print(img_width) 
template_height, template_width = template.shape
print (template_height)
print (template_width)

print ('No estoy colgado solo soy lento, espere por favor')
# Crea una matriz para almacenar los resultados de la convolucion:

result = np.zeros((img_height - template_height, img_width - template_width))

# Realiza el template matching utilizando la distancia euclidiana:

for y in range(img_height - template_height):
    for x in range(img_width - template_width):
        roi = img[y:y + template_height, x:x + template_width]  # Extrae la region de interes (ROI)
        diff = template - roi  # Calcula la diferencia entre el template y la ROI
        distance = np.sqrt(np.sum(np.square(diff)))  # Calcula la distancia euclidiana
        result[y, x] = distance

# Encuentra la ubicacion del mejor ajuste:
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
best_match_loc = min_loc  # Cambiar a max_loc si se desea encontrar el peor ajuste

# Dibuja un rectangulo en la ubicacion del mejor ajuste de grosor 4
top_left = best_match_loc
bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
cv.rectangle(img, top_left, bottom_right, 255, 4)  # Dibuja el rectangulo

# Muestra la imagen resultante en la ventana creada al inicio

cv.imshow('Resultado', img)
cv.imwrite('salida.png', img)
end_time = time.perf_counter ()
print(end_time - start_time, "seconds")
cv.waitKey(0)
cv.destroyAllWindows()

# lor archivos 'imagen.jpg' y 'template.jpg',se encuentran en el mismo directorio del script.
# la implementacion es muy costosa por los for anidados en imagenes grandes