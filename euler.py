def e_cuadratica(numero):
	"""Funcion para calcular aproximaciones del valor euler.
	E: Un numero entero positivo y mayor que cero
	S: Un numero o un error
	R: Ocupa numero entero positivo y mayor que cero"""
	if type(numero) != int:
		return "Error01"
	elif numero < 0:
		return "Error02"
	else:
		resultado = 0
		while numero >= 0:
			factorial = 1
			i= numero
			while i > 0:
				factorial = factorial * i
				i = i - 1 
			resultado = resultado + (1/factorial)
			numero = numero - 1
		return resultado


def e_lineal(numero):
	"""Funcion para calcular aproximaciones del valor euler.
	E: Un numero entero positivo y mayor que cero
	S: Un numero o un error
	R: Ocupa numero entero positivo y mayor que cero"""
	if type(numero) != int:
		return "Error01"
	elif numero < 0:
		return "Error02"
	elif numero == 0:
		return 1
	else:
		resultado = 0
		factorial = 1
		i = numero
		while i > 0:
			factorial = factorial * i
			i = i - 1
		resultado = resultado + (1/factorial)
		return resultado + e_lineal(numero - 1)

