
from src.figuras import crear_tricilindro
from src.volumenes import calcular_volumen, graficar_figura

# =========================
# Parámetros
# =========================

radio = 2
n = 80

# =========================
# Crear figura
# =========================

X, Y, Z, figura = crear_tricilindro(radio, n)

# =========================
# Calcular volumen
# =========================

volumen = calcular_volumen(figura, radio, n)

print(f"\nVolumen aproximado: {volumen:.4f}")

# Volumen teórico
volumen_teorico = 8 * (2 - 2**0.5) * radio**3

print(f"Volumen teórico: {volumen_teorico:.4f}")

# Error
error = abs(volumen - volumen_teorico)

print(f"Error: {error:.4f}")

# =========================
# Graficar
# =========================

graficar_figura(
    X,
    Y,
    Z,
    figura,
    f"Tricilindro de radio {radio}"
)
