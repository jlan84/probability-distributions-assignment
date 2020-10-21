import scipy.stats as stats
import math

if __name__ == "__main__":

    #1 Poisson 13.5%
    lam = 2
    poisson = stats.poisson(mu=lam)
    print(poisson.pmf(0))

    #2 Binomial 28.5%
    n = 20
    k = 2
    p = 0.1
    binomial = stats.binom(n=20, p=0.1)
    print(binomial.pmf(2))

    #3 Binomial 67.6%
    print(binomial.cdf(2))

    #4 Poisson 22.3%
    lam = 30/60*3
    poisson = stats.poisson(mu=lam)
    print(poisson.pmf(0))
    
    #5 Exponential 20.1%
    lam = .08*2
    exp = stats.expon(scale=1/lam)
    print(1-exp.cdf(10))
    cdf = 1 - math.exp(-10*lam)
    print('!!',1-cdf)

    #6 Uniform 25%
    
    uniform = stats.uniform(loc=10, scale=20)
    print(1 - uniform.cdf(25))

    #7 Poisson 0.8%
    p = 1/5
    k = 0
    lam = -3*math.log(p)
    poisson = stats.poisson(mu=lam)
    print(poisson.pmf(0))

    #8 Hypergeometric 86.7%
    N = 14
    K = 7
    n = 5
    k = 2
    hypergeometric = stats.hypergeom(M=N, n=K, N=n)
    print(1-hypergeometric.cdf(1))


    
