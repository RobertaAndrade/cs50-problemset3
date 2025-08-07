# solicita ao user uma fração formatada como X/Y um para cada inteiro possível e exibe uma porcentagem arredondada para cada valor inserido

# se restar 1% ou menos: exibe E (empty) | se restar 99% ou mais: exibe F (full).
# se X ou Y não for um inteiro | X for > que Y | Y for <= 0 | X for < 0: solicita input novamente
# captura exceções como ValueError | ZeroDivisionError
# split divide a str em partes a partir do separador passado como parâmetro, e então retorna numa lista
# Formatted String Literals (f-strings) -> from fractions import Fraction -> f'{Fraction(1, 3)}'
# https://docs.python.org/3/library/stdtypes.html#string-methods

from fractions import Fraction

def main():
    while True:
        try:
            fracao = input("Fraction: ")
            x, y = fracao.split("/") # possivel comprimir numa linha usando map, ex -> x, y = map(int, fracao.split("/"))
            x = int(x)
            y = int(y)

            if x > y or y <= 0 or x < 0:
                continue

            fracao = Fraction(x, y)
            porcentagem = round(fracao * 100)

            if porcentagem <= 1:
                print("E")
            elif porcentagem >= 99:
                print("F")
            else:
                print(f"{porcentagem}%")
            break

        except (ValueError, ZeroDivisionError):
            continue

main()
