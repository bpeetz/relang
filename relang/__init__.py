from prompt_toolkit import prompt
import relang


class Relang:
    def __init__(self, text):
        self.ALL_POSSIBLE_DIGITS = list(map(str, [i for i in range(0, 10)]))
        self.ALL_POSSIBLE_OPERATORS = ["-", "+", "/", "*", "^"]
        self.text = text
        self.cursor = 0

    def peek(self):
        if len(self.text) > 0 and self.cursor < len(self.text):
            return self.text[self.cursor]
        else:
            return None

    def pop(self):
        output = self.text[self.cursor]
        self.cursor += 1
        return output

    def expect(self, char_expected):
        if self.peek() in char_expected:
            return True
        else:
            raise ValueError(
                f'Got {self.peek()}, but expected one of: {", ".join(char_expected)}'
            )

    def remove_whitespace(self):
        while self.peek() == " ":
            self.pop()

    # Parse functions
    def parse_whole_number(self):
        self.remove_whitespace()
        output = 0
        while self.peek() in self.ALL_POSSIBLE_DIGITS:
            output *= 10
            output += int(self.pop())
        return str(output)

    def parse_operator(self):
        self.remove_whitespace()
        if self.expect(self.ALL_POSSIBLE_OPERATORS):
            return self.pop()

    def parse_term(self):
        output = ""
        while self.peek() != None:
            output += self.parse_whole_number()
            if self.peek() != None:
                output += self.parse_operator()
        return output


def main():
    while True:
        relang = Relang(prompt("Rechenausdruck: "))

        try:
            number = relang.parse_term()
            print(f"Parsed number: {number}")
        except ValueError as err:
            print(f"parse failed: {err}")


main()
