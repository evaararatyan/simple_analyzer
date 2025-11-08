class Analyzer:
    def __init__(self):
        self.numbers = []

    def add_number(self, x):
        self.numbers.append(x)

    def even_count(self):
        return sum(1 for n in self.numbers if n % 2 == 0)

    def odd_count(self):
        return sum(1 for n in self.numbers if n % 2 != 0)

    def highest_number(self):
        return max(self.numbers) if self.numbers else None

    def increasing_pairs(self):
        return sum(1 for i in range(1, len(self.numbers)) if self.numbers[i] > self.numbers[i-1])

