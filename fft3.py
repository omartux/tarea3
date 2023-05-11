import cv2
import numpy as np

def fft2_iterative(img):
    # Obtiene las dimensiones de la imagen
    height, width = img.shape

    # Calcula el número de puntos de datos en la FFT2
    num_points = height * width 

    # Realiza la transformada en la primera dimensión (filas)
    for i in range(height):
        img[i, :] = np.fft.fft(img[i, :])

    # Realiza la transformada en la segunda dimensión (columnas)
    for j in range(width):
        img[:, j] = np.fft.fft(img[:, j])

    return img

# Carga la imagen del template
template = cv2.imread('template.jpg', 0)

# Verifica si la imagen se cargó correctamente
if template is None:
    print("Error al cargar la imagen.")
else:
    # Aplica la FFT2 utilizando enfoque iterativo
    fft_result = fft2_iterative(template.astype(np.complex128))

    # Muestra la parte real y la parte imaginaria de la FFT2
    magnitude_spectrum = 20 * np.log(np.abs(fft_result))
    phase_spectrum = np.angle(fft_result)

    cv2.imshow('original',template)
    cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))
    cv2.imshow('Phase Spectrum', phase_spectrum.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
