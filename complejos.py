import math

# el número complejo se representa como (a, b) donde:
# a = parte real, b = parte imaginaria

def suma(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def resta(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def producto(c1, c2):
    real = c1[0]*c2[0] - c1[1]*c2[1]
    imag = c1[0]*c2[1] + c1[1]*c2[0]
    return (real, imag)

def division(c1, c2):
    denom = c2[0]**2 + c2[1]**2
    if denom == 0:
        raise ZeroDivisionError("División por cero en números complejos")
    real = (c1[0]*c2[0] + c1[1]*c2[1]) / denom
    imag = (c1[1]*c2[0] - c1[0]*c2[1]) / denom
    return (real, imag)

def modulo(c):
    return math.sqrt(c[0]**2 + c[1]**2)

def conjugado(c):
    return (c[0], -c[1])

def fase(c):
    return math.atan2(c[1], c[0])

# Conversión entre cartesiano y polar
def cartesiano_a_polar(c):
    r = modulo(c)
    theta = fase(c)
    return (r, theta)

def polar_a_cartesiano(p):
    r, theta = p
    real = r * math.cos(theta)
    imag = r * math.sin(theta)
    return (real, imag)
