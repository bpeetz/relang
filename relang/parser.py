class Parser:
    def __init__(self, text):
        self.DIGITS = list(map(str, [i for i in range(0, 10)]))
        self.OPERATORS = ["-", "+", "/", "*", "^"]
        self.NUMBER_SEPARATORS = [",", "."]

        self.text = text.replace(" ", "")
        self.cursor = 0
        if len(self.text) == 0:
            print("No input given.")

    def _peek(self):
        if len(self.text) > 0 and self.cursor < len(self.text):
            return self.text[self.cursor]
        else:
            return None

    def _pop(self):
        output = self.text[self.cursor]
        self.cursor += 1
        return output

    def _expect(self, char_expected):
        if self._peek() in char_expected:
            return True
        elif self._peek() is None:
            return False
        else:
            raise ValueError(
                f'Got {self._peek()}, but expected one of: {", ".join(char_expected)}'
            )

    # Parse functions
    def _parse_whole_number(self):
        output = 0
        while self._expect(
            self.DIGITS
            + self.OPERATORS
            + self.NUMBER_SEPARATORS
            + ["e", "E"]
        ):
            if (
                self._peek()
                in self.OPERATORS + self.NUMBER_SEPARATORS  + ["e", "E"]
                or self._peek() is None
            ):
                break
            output *= 10
            output += int(self._pop())
        return str(output)

    def _parse_signed_number(self):
        sign = 1
        if self._peek() in ["-", "+"] + self.DIGITS:
            if self._peek() == "-":
                sign = -1
                self._pop()
            elif self._peek() == "+":
                self._pop()
        output = float(self._parse_number()) * sign
        return str(output)


    def _parse_number(self):
        output = self._parse_whole_number()

        if self._peek() in self.NUMBER_SEPARATORS:
            self._pop()
            output += "."
            output += self._parse_whole_number()

        if self._peek() in ["E", "e"]:
            self._pop()
            self._expect(["+", "-"] + self.DIGITS)
            if self._peek() in ["+"] + self.DIGITS:
                sign = 1
                if self._peek() == "+":
                    self._pop()
            elif self._peek() == "-":
                sign = -1
            output = float(output) * 10 ** (int(self._parse_whole_number()) * sign)
        return output

    def _parse_operator(self):
        self._remove_whitespace()
        if self._expect(self.OPERATORS):
            return self._pop()
