import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        # z = z*z + 1./c
        z = z*z + c
        n += 1
    if n == max_iter:                                   #if reach max_iter
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))              #if not reach max_iter, return this

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    C = np.array([[complex(a, b) for a in x] for b in y])
    
    mandelbrot_output = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            mandelbrot_output[i, j] = mandelbrot(C[i, j], max_iter)

    return mandelbrot_output

def plot_mandelbrot_set(mandelbrot_output):

    plt.imshow(mandelbrot_output, cmap='jet', extent=[x_min, x_max, y_min, y_max])
    # plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

if __name__ == "__main__":

    width, height = 1920, 1080
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    max_iter = 100

    # 创建复数平面上的网格
    plt.grid(True, linestyle='--', linewidth=0.5, color='white', which='major', axis='both')
    plt.grid(True, linestyle=':', linewidth=0.5, color='gray', which='minor', axis='both')
    plt.minorticks_on()
    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.1))

    mandelbrot_output = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
    plot_mandelbrot_set(mandelbrot_output)
