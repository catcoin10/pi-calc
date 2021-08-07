# pi fraction calculator
# try to find fractions that have more information about pi encoded than that amount of information in pi itself
# this uses logarithms to calculate the amount of information stored
from mpmath import *
import sys

mp.dps = 120 # go to 100 just in case could easily be way less -- like <25
global Pi
Pi = +pi

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

# how much data is in this number?
def data_count(n):
	pi_multiple = int(n*Pi) + 1
	pi_divide = pi_multiple / n
	log_diff = log(abs(pi_divide-Pi), 10) * -1
	information_content = log((pi_multiple*n), 10)
	log_n = log(n, 10)
	return (log_diff - information_content) #+ log_n

def pi_multiply(n):
	return int(n*Pi) + 1


def data_find(min_quit):
	count = 0
	n = start_n = int(sys.argv[2])
	distance = -2 # start program at -2 and then chnage
	while distance < min_quit: # this is the minimum required to quit
		distance = data_count(n)
		n = nextprime(n) # increment
		count += 1
		if (count % 10**4)==0:	print(n)
	return [n, pi_multiply(n), str(distance)[:12]]


x = sys.argv[1]
print(data_find(mpf(x)))
