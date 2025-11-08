    def average_number(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def range_diff(self):
        return max(self.numbers) - min(self.numbers) if self.numbers else 0
 
