class equation:
    ops = ['+', '*', '||']

    def __init__(self, data):
        data = data.split(': ')
        self.target = int(data[0])
        self.numbers = list(map(int, data[1].split()))
        self.operators = []
        for i in range(1, len(self.numbers)):
            self.operators.append('+')

    def evaluate(self):
        numbers = []
        operators = []
        for i in range(len(self.operators)):
            if self.operators[i] == '||':
                numbers.append(int(str(self.numbers[i]) + str(self.numbers[i+1])))
            else:
                numbers.append(self.numbers[i+1])
                operators.append(self.operators[i])
                if i == len(self.operators) - 1:
                    numbers.append(self.numbers[i+1])
        print(self.string(numbers, operators))
        value = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                value += numbers[i+1]
            else:
                value *= numbers[i+1]
        return value
    
    def find_valid(self, next=0):
        print(self.string(), '=', self.evaluate(), '|', self.target)
        if self.evaluate() == self.target:
            print('found')
            return True
        for i in range(next, len(self.operators)):
            self.swaperators(i)
            if self.find_valid(i + 1):
                return True
            self.swaperators(i)
            if self.find_valid(i + 1):
                return True
            self.swaperators(i)
        return False
    
    def swaperators(self, i):
        if self.operators[i] == '+':
            self.operators[i] = '*'
        elif self.operators[i] == '*':
            self.operators[i] = '||'
        else:
            self.operators[i] = '+'
    
    def string(self, numbers=None, operators=None):
        if numbers is None:
            numbers = self.numbers
        if operators is None:
            operators = self.operators
        s = f"{numbers[0]}"
        for i in range(len(operators)):
            s += f" {operators[i]} {numbers[i+1]}"
        return s