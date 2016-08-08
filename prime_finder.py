from decimal import *

class PrimeFinder:

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

user_input = int(raw_input("Enter a number to check for primality: "))

print "Is it prime?", PrimeFinder.is_prime(user_input)

