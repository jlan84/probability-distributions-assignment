import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def profit():
    views = int(stats.uniform(loc=5000, scale=1000).rvs())
    conversions = stats.binom(n=views, p=0.12).rvs()
    wholesales = stats.binom(n=conversions, p=0.2).rvs()
    retail = conversions - wholesales
    profit = wholesales*50 + retail*60
    return profit



if __name__ == "__main__":
    samples = [profit() for i in range(10000)]

    print(f'2.5% percentil: {np.percentile(samples, 2.5)}')
    print(f'97.5% percentil: {np.percentile(samples, 97.5)}')
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30)
    plt.show()