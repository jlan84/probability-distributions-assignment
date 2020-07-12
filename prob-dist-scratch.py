import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


#1

poisson = stats.poisson(mu=2)
print(poisson.pmf(0))

#2

binomialBox = stats.binom(n=20, p=0.1) 
print(binomialBox.pmf(2))

#3

print(binomialBox.cdf(2))

#4

poissonBar = stats.poisson(mu=1.5)
print(poissonBar.pmf(0))

#5

lam = .08*2
exponentialCookies = stats.expon(scale=1/.16)
print('5:', 1 - exponentialCookies.cdf(10))

#6
uniformFlight = stats.uniform(loc=10, scale=20)
print(1 - uniformFlight.cdf(25))

#7
poissonMeows = stats.poisson(mu=4.8)
print(poissonMeows.pmf(0))


#8
hyperForks = stats.hypergeom(M=14, n=7,N=5)
print(1 - hyperForks.cdf(1))