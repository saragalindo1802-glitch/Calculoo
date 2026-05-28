import numpy as np

def crear_tricilindro(radio, n):

    limite = radio

    puntos = np.linspace(-limite, limite, n)

    X, Y, Z = np.meshgrid(
        puntos,
        puntos,
        puntos
    )

    cilindro_z = (X**2 + Y**2 <= radio**2)

    cilindro_x = (Y**2 + Z**2 <= radio**2)

    cilindro_y = (X**2 + Z**2 <= radio**2)

    tricilindro = (
        cilindro_z &
        cilindro_x &
        cilindro_y
    )

    return X, Y, Z, tricilindro.astype(float)
