# Random Variables and Their Distributions

In this assignment, we will work with some common probability distributions.

## Part 1: Identifying Distributions

Often we have to identify what distribution we should use to model a real-life
situation. This exercise well get you some practice doing so.

For each question:

- Name the most appropriate distribution and the associated parameter(s)
- Set up equation for the distribution, e.g.

  ```
  Let X be the number of heads in 30 coin flips:
  X ~ Binomial(n=30, p=0.5)
  ```

- Use the pdf/pmf of the distribution to calculate the desired probability, e.g.

  ```
  P(X = 15) = 0.144
  ```

  You may calculate these probabilities either by hand (with an assist from wikipedia to look up the PMF or CDF), or use python:

  ```
  import scipy.stats as stats
  dist = stats.binom(n=30, p=0.5)
  print("P(X = 15) = ", dist.pmf(15))
  ```

<br>

1. A typist makes on average 2 mistakes per page.  What is the probability of a particular page having no errors on it?

2. Components are packed in boxes of 20. The probability of any individual component being
   defective is 0.1. What is the probability of a box containing exactly 2 defective components?

3. Components are packed in boxes of 20. The probability of any individual component being
   defective is 0.1. What is the probability of a box containing AT MOST 2 defective components?

4. Patrons arrive at a local bar at a rate of 30 per hour. What is the probability that the bouncer can take a three minute bathroom break without missing the next patron?

5. You need to find a tall person, at least 6 feet tall, to help you reach a cookie jar. 8% of the population is 6 feet or taller, and people pass by on average twice per minute.  If you wait on the sidewalk, what is the probability that you will have to wait longer than ten minutes to get some cookies?

6. A harried passenger will be several minutes late for a scheduled 10 A.M. flight to NYC. Nevertheless, he might still make the flight, since boarding is always allowed until 10:10 A.M., and boarding is sometimes permitted up to 10:30 AM.

Assuming the end time of the boarding interval is **uniformly distributed** over the above limits, find the probability that the passenger will make his flight, assuming he arrives at the boarding gate at 10:25.

7. Your cat starts to beg for dinner at 3:30 every day, and you suspect that it meows at a fixed rate. You've observed that about one fifth of the time your cat will not meow until 3:40, giving you 10 unexpected minutes of quiet. What is the probability your cat leaves you alone for 30 minutes?

8. Somehow you ended up with two types of forks.  There are the good forks, which are big and fit a healthy bite, but there are also these small, thin ones that you don't really understand what they are for, you should probably just get rid of them.  You need two forks for you and your partner, and grab a fistful of 5.  If there are 14 forks in the drawer, of which half are the good kind, what is the probability you have at least your two required good forks?


## Part 2: Distribution Simulation

Often times in real life applications, we can specify the values of a variable to be drawn from a particular distribution.
For example the number of sales made in the next month can be modeled as a uniform distribution over the range of
5000 and 6000 (the terminology here is that the number of sales is a *random variable*, and its *distribution* is uniform).

In this scenario, we are modeling `profit` as a product of `number of views`, `conversion` and `profit per sale`,
where `number of views`, `conversion` and `profit per sale` can be modeled as random variables.
By randomly drawing values from these distributions, we are able to get a distribution of the range of `profit`
based on the uncertainties in the other variables.

`Profit = Number of views * Conversion * (Wholesale_Proportion * 50 +
(1 - Wholesale_Proportion)*60)`

The assumptions of our model are:

- `Number of views` is a uniform distribution over the range of 5000 and 6000.
- `Conversion` is binomially distributed where the probability of success is `0.12` for each view.
- Profit per sale can take on two values: 50 for wholesale and 60 for non-wholesale. There is a 0.2 probability of a sale being wholesale and 0.8 probability of being non-wholesale. You should be able to model both the number of wholesale sales and the number of non-wholesales sales as binomial distributions (but one of the parameters of this distribution is not fixed, it depends on an earlier random quantity).

1. Given the distributions of each of variables, use `scipy` to write a function that would draw random values from each of the
   distributions to simulate draws from the distribution of `profit`

2. Draw 10,000 samples from the distribution of profit, and plot a histogram.  Does it look like any of the common distributions is a good fit for `profit`?

3. Compute the range of values of `profit` where the middle 95% of the probability mass lies.
