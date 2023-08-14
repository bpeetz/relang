from prompt_toolkit import prompt
from parser import Parser


def main():
    while True:
        parser = Parser(prompt("Rechenausdruck: "))

        try:
            print(f"Parsed output: {parser._parse_signed_number()}")
        except ValueError as err:
            raise err
            # print(f"parse failed: {err}")


main()
