from decimal import *


class PrimeFinder:

    def __init__(self, precision=170):
        self.set_precision(precision)
        self.eulers_string = str(Decimal(1).exp())

    @staticmethod
    def set_precision(precision):
        getcontext().prec = precision

    def prime_of_length(self, count, size):
        total_count = 0
        for n in range(2, len(self.eulers_string) - size):
            number = int(self.eulers_string[n: n + size])
            if self.is_prime(number):
                total_count += 1
            if total_count == count:
                return number
        return -1

    @staticmethod
    def is_prime(num):
        if num == 2 or num == 3:
            return True
        if num < 2 or num % 2 == 0 or num % 3 == 0:
            return False
        if num < 11:
            return True

        root = int(num**0.5)
        x = 5
        while x <= root:
            if num % x == 0:
                return False
            if num % (x + 2) == 0:
                return False
            x += 6
        return True


