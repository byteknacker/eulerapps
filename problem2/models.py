"""Solution to Project Euler's Problem 2: Even Fibonacci Numbers.

Classes:

Fibo(base1, base2):
    base1: the first base number of the Fibonacci series
    base2: the second base number of the Fibonacci series

    Methods of Fibo:

    createFibolist(index_limit):
        Create a list of Fibonacci numbers with index_limit elements

        index_limit: the maximum number of elements in the list of
        Fibonacci series

    createFibolistbyValue(value_limit):
        Create a list of Fibonacci numbers where the last element is
        less or equal to value_limit

        value_limit: the maximum allowed value for the last element
        in the list of Fibonacci numbers
"""

from django.db import models


class Fibo(models.Model):
    """Fibonacci series generator."""

    value_limit = models.FloatField()
    evensum = models.FloatField()

    def __str__(self):
        """Return on print list of all instance attributes."""
        return str([self.value_limit, self.evensum])

    def createFibolistbyValue(self, value_limit):
        """Create a list of Fibonacci numbers: last element <= value_limit."""
        fibolist = [1, 2]
        iterator = 0
        nextbase = 0
        while nextbase < value_limit:
            nextbase = fibolist[0 + iterator] + fibolist[1 + iterator]
            fibolist.append(nextbase)
            iterator += 1
        fibolist.pop(-1)
        return fibolist

    def evenFibolist(self, value_limit):
        """Create a list of even Fibonacci numbers up to value_limit."""
        fibolisteven = Fibo.createFibolistbyValue(self, value_limit)
        for oddnumber in fibolisteven[:]:
            if oddnumber % 2 != 0:
                fibolisteven.remove(oddnumber)
        return fibolisteven

    def evenFiboSum(self):
        """Create the sum of all even Fibonacci numbers up to value_limit."""
        value_limit = self.value_limit
        evensumlist = Fibo.evenFibolist(self, value_limit)
        evensum = sum(evensumlist)
        self.evensum = evensum
        return self.evensum
