from decimal import *


class PrimeFinder:
    """ Class object to handle searching for primes

     Object contains methods for determining if a
     number is a prime and for finding the Xth
     occurrence of a Y-digit prime.
    """

    def __init__(self, precision=200):
        """ Initializes object with default precision set to 200

        Default class initialization will include a default digit
        precision of 200. The :precision parameter allows the object
        to set how far out Euler's Number is needed. A conservative
        200 is set by default, but the :Decimal object can carry a
        precision to 1000. If no precision is set, default is 28.

        :Decimal(1).exp() will return e ** 1, that is Euler's Number
        to the exponent value of 1, using the preset precision.
        Convert the resultant number into a string, :eulers_string,
        for easy parsing through the digits.

        :param precision: level of precision to set for search
        """
        self.set_precision(precision)
        self.eulers_string = str(Decimal(1).exp())

    @staticmethod
    def set_precision(precision):
        """ Sets the precision of Decimal object

         This probably won't work outside of initialization for now,
         but will likely complete at a later time for fun.

         Sets the precision of the Decimal object, how far out a value
         should be calculated. The default precision when not set is 28.

        :param precision: level of precision
        :return: no return
        """
        getcontext().prec = precision

    def prime_of_length(self, count, size):
        """ Returns Xth Y-digit prime in Euler's Number

        Given :count of :size-digit primes, finds the :count occurrence
        of a prime of :size digits. Starting at just after the decimal,
        check integers of :size digits against is_prime() to determine
        primality. For each prime of that size, increment :total_count;
        once :total_count reaches the value of :count, the current prime
        is the prime we're looking for. If that doesn't happen, then
        default to returning -1.

        :param count: occurrence of any primes
        :param size: digit length of any primes
        :return: :count occurrence of :size-digit prime if found,
        otherwise return -1
        """
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
        """ Returns true if :num is prime, false otherwise

        Given :num, determine if it is a prime or not. Eliminate
        easy non-primes; numbers less than 2, divisible by 2 or
        divisible by 3. Given those checks, anything less than 11
        is a prime and can return true by default.

        No need to check anything greater than sqrt(:num) to
        determine primality. Explained well on StackOverflow, here:
        http://goo.gl/WcqxNK

        Admittedly, it's at this level of optimization that I
        would've stopped. The remaining check done at intervals of
        +6 and +8 are optimizations I hadn't known about but found
        online. I am including them, not that I need them in this
        case, because I thought they were neat and wanted to disclose
        it. StackOverflow post about it: http://goo.gl/3AHR7h

        :param num: number to be checked for primality
        :return: true if :num is prime, false otherwise
        """
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


