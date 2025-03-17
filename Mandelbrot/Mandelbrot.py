# генерация фрактального изображение Мандельброта - один из самых красивых и известных математических объектов
# у фракталов есть ф-я. свмоподобия, то бишь их структура повторяется при маштабировании

import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    # массив для хранения результатов
    mandelbrot_set = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            # координаты пикселя в комплексное число
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            c = complex(real, imag)

            # кол-во итераций для данного комплексного числа
            mandelbrot_set[y, x] = mandelbrot(c, max_iter)

    return mandelbrot_set


# параметры для генерации изображения
width, height = 800, 600
x_min, x_max = -2.5, 1.5
y_min, y_max = -1.5, 1.5
max_iter = 100

# ген множество Мандельброта
mandelbrot_image = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# юз матлотлиб для отображения изображения
plt.imshow(mandelbrot_image, cmap='hot', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Множество Мандельброта")
plt.show()
