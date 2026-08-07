# Guia de Trabajo 1
# Punto 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# FUNCION PARA CONSTRUIR EL CAMPO DE PENDIENTES

def campo_pendientes(ax, f, xlim=(-5, 5), ylim=(-5, 5), h=0.5):

    m = np.arange(xlim[0], xlim[1] + h, h)
    n = np.arange(ylim[0], ylim[1] + h, h)

    X, Y = np.meshgrid(m, n)

    pendiente = f(X, Y)

    norm = np.sqrt(1 + pendiente**2)

    U = 1 / norm
    V = pendiente / norm

    ax.quiver(
        X, Y, U, V,
        angles='xy',
        color='navy',
        alpha=0.6
    )

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.grid(alpha=0.2)
