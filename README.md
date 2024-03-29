# Apps developed for Project Euler

Here are the solutions to some riddles on Project Euler as web apps in Django

https://projecteuler.net/

## Problem 2: Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

### Solution to Problem 2
4613732

## Problem 7: 10,001st Prime

The solution to this problem is located in the script problem7.py.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10,001st prime number?

### Approach to Problem 7

First we need to find an algorithm that can find prime numbers fast and
repetitively.

Then we generate a list with the elements being the prime numbers, after
which we stop when the length of the list exceeds 10001. Tweak around
this to make sure that we can get a list with the last element being the
10001st prime number.

This may be inefficient but should work. The more efficient way is to just
find the 10001st prime number at the end of the algorithm. But as we know,
there is absolutely no formula yet found to generate prime numbers
based on their index number. So we just have to brute force it with an
algorithm and whether or not we store them in a list is not that much of
relevance.
