from prompt_toolkit import prompt
from relang import Relang


def main():
    while True:
        relang = Relang(prompt("Rechenausdruck: "))

        try:
            number = relang.parse_term()
            print(f"Parsed number: {number}")
        except ValueError as err:
            print(f"parse failed: {err}")


main()
