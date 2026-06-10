import os

# Bot de optimización debería quejarse de este desorden de espacios
def   suma(a,   b):
    return a + b

# Esta variable no se usa en ningún lado, el bot lo va a notar
variable_muerta = "no sirvo para nada"

# El bot de funcionamiento va a revisar que esto compile bien
print("La suma de 5 + 5 es:", suma(5, 5))
