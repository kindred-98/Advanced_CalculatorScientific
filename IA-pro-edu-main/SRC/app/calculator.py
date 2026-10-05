import math
import operator

# =========================
# MENSAJES DE ERROR
# =========================
ERROR_DIVISION_CERO = "Error: No se puede dividir entre 0"
ERROR_RAIZ_NEGATIVA = "Error: raíz negativa"
ERROR_LOG_INVALIDO = "Error: log inválido"
OPERACION_INVALIDA = "Operación no válida"


# =========================
# OPERACIONES CON VALIDACIÓN
# =========================
def dividir(num1, num2):
    if num2 == 0:
        return ERROR_DIVISION_CERO
    return num1 / num2


def raiz(num1, num2):
    if num1 < 0:
        return ERROR_RAIZ_NEGATIVA
    return math.sqrt(num1)


def logaritmo(num1, num2):
    if num1 <= 0:
        return ERROR_LOG_INVALIDO
    return math.log(num1)


# =========================
# TABLA DE OPERACIONES
# =========================
OPERACIONES = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": dividir,
    "^": operator.pow,
    "√": raiz,
    "sin": lambda num1, num2: math.sin(num1),
    "cos": lambda num1, num2: math.cos(num1),
    "log": logaritmo,
    "exp": lambda num1, num2: math.exp(num1),
}


# =========================
# FUNCIÓN CALCULAR
# =========================
def calcular(num1, num2, operacion):

    funcion = OPERACIONES.get(operacion)

    if funcion is None:
        return OPERACION_INVALIDA

    return funcion(num1, num2)