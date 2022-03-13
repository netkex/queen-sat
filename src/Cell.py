class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_num(self, n):
        return self.x * n + self.y + 1

    @staticmethod
    def from_num(num, n):
        num -= 1
        return Cell(num // n, num % n)

    def __str__(self):
        return f"({self.x}, {self.y})"
