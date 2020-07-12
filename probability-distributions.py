import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

#Part 1
#1
poisson = stats.poisson(mu=2)
print(f'P(X=0) is {poisson.pmf(0)}')

#2
binomial = stats.binom(n=20, p=0.1)
print(f'P(X=2) is {binomial.pmf(2)}')

#3
print(f'P(X<=2) is {binomial.cdf(2)}')

#4
poisson = stats.poisson(mu=1.5)
print(f'P(X=0) is {poisson.pmf(0)}')

#5
exponent = stats.expon(scale=6.25)
print(f'P(X>10) is {1-exponent.cdf(10)}')

#6
uniform_dist = stats.uniform(loc=10, scale=20)
print(f'P(X=25)  is {1 - uniform_dist.cdf(25)}')

#7
poisson = stats.poisson(mu=4.8)
print(f'P(X=0) is {poisson.pmf(0)}')

#8
hyper = stats.hypergeom(M=14, n=, N=5) #M = N total count n = K number of the interested amount N = n sample size
print(f'P(X=2) is {1 - hyper.cdf(1)}')

#Part 2
def prof():
    views = int(stats.uniform(loc=5000, scale=1000).rvs())
    conversion = stats.binom(p=.12, n=views).rvs()
    wholesale = stats.binom(p=.2,n=conversion).rvs()
    not_wholesale = conversion - wholesale
    profit = (wholesale*50 + not_wholesale*60)
    return profit

# sample = [prof() for _ in range(10000)]

# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.hist(sample)
# plt.show()


