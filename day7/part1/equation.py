class equation:
    def __init__(self, data):
        data = data.split(': ')
        self.target = int(data[0])
        self.numbers = list(map(int, data[1].split()))
        self.operators = []
        for i in range(1, len(self.numbers)):
            self.operators.append('+')

    def evaluate(self):
        value = self.numbers[0]
        for i in range(len(self.operators)):
            if self.operators[i] == '+':
                value += self.numbers[i+1]
            else:
                value *= self.numbers[i+1]
        return value
    
    def find_valid_old(self):
        print(self.string(), '=', self.evaluate(), '|', self.target)
        if self.evaluate() == self.target:
            print('found')
            return True
        for i in range(len(self.operators)):
            for j in range(i, len(self.operators)):
                self.swaperators(j)
                print(self.string(), '=', self.evaluate(), '|', self.target)
                if self.evaluate() == self.target:
                    print('found')
                    return True
                self.swaperators(j)
            self.swaperators(i)
        # print(self.string(), '=', self.evaluate(), '|', self.target)
        # print('not found')
        return False
    
    def find_valid(self, next=0):
        # print(self.string(), '=', self.evaluate(), '|', self.target)
        if next == len(self.operators):
            return False
        if self.evaluate() == self.target:
            # print('found')
            return True
        for i in range(next, len(self.operators)):
            self.swaperators(i)
            if self.evaluate() == self.target:
                # print('found')
                return True
            if self.find_valid(i + 1):
                return True
            self.swaperators(i)
        return False
    
    def swaperators(self, i):
        if self.operators[i] == '+':
            self.operators[i] = '*'
        else:
            self.operators[i] = '+'
    
    def string(self):
        s = f"{self.numbers[0]}"
        for i in range(len(self.operators)):
            s += f" {self.operators[i]} {self.numbers[i+1]}"
        return s