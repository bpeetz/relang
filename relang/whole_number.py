from parser import Parser


class WholeNumber(Parser):
    def __init__(self, input):
        super().__init__(input)
        output = 0
        while self._peek() in self.ALL_POSSIBLE_DIGITS:
            output *= 10
            output += int(self._pop())
        self.number = output
