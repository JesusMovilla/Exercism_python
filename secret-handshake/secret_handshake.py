def commands(number):
    clave = ['wink', 'double blink', 'close your eyes', 'jump']
    combinacion = [action for index,
                   action in enumerate(clave) if 2 ** index & number]
    return combinacion[::-1] if 2 ** 4 & number else combinacion
