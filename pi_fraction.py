# pi fraction calculator
# try to find fractions that have more information about pi encoded than that amount of information in pi itself
# this uses logarithms to calculate the amount of information stored
from mpmath import *
import sys

mp.dps = 120 # go to 100 just in case could easily be way less -- like <25
global Pi, pistr
Pi = +pi
pistr = str(Pi)

# check if a number is prime
def isprime(n):
	max = int(n**0.5)+1 # we only need to count to sqrt
	prime = True # guilty of being prime until proven innocent
	if n == 1:	return None
	if n == 2:	return True
	for i in range(3, max, 2):
		if (n % i) == 0:
			prime = False
			continue
	return prime # fallthrough if we don't get here

# what is the prime after a number
def nextprime(n):
	if isprime(n):		n += 2 # just in case the program won't make this mistake
	while not isprime(n):	n += 2 # simple while loop that adds to number
	return n

def pi_multiply(n): # this number gets us as close to pi as we can as far as we know
	return int(n*Pi) + 1

# how much digits match Pi here?
def digit_count(n):
	x = mpf(pi_multiply(n)/n) # what is the answer?
	x = str(x) # make a string
	digits_alike = 0 # also the index, somewhat misnomer
	for i in pistr:
		if i == x[digits_alike]: digits_alike += 1
		else:			break
	return digits_alike - 2 + 1 # exclude "3.", but remember we count from 0

def data_find():
	x = 115 # start above the only known example: 113 -- we can change it or even multithread with modulus but still
	count = 0
	digits = len(str(pi_multiply(x))) + len(str(x))
	while digit_count(x) < digits:
		x = nextprime(x)
		digits = len(str(pi_multiply(x))) + len(str(x))
		count += 1
		if (count % 100000) == 0: print(x)
	return [x, pi_multiply(x)]



print(data_find())
