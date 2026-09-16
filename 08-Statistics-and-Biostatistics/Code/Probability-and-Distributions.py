"""
Probability and Distributions
-----------------------------

This script demonstrates basic probability calculations
and commonly encountered probability distributions.

Topics:
- Basic probability
- Complementary probability
- Binomial distribution
- Normal distribution
- Mean and standard deviation

The examples are presented in a biological context.
"""

import math


# ---------------------------------------------------------
# 1. Basic Probability
# ---------------------------------------------------------

# Suppose 30 out of 100 biological samples show a
# particular characteristic.

total_samples = 100
positive_samples = 30

probability_positive = positive_samples / total_samples

print("Basic Probability")
print("-----------------")
print("Probability of positive observation:",
      probability_positive)


# ---------------------------------------------------------
# 2. Complementary Probability
# ---------------------------------------------------------

# Probability of an event not occurring.

probability_negative = 1 - probability_positive

print("\nComplementary Probability")
print("------------------------")
print("Probability of negative observation:",
      probability_negative)


# ---------------------------------------------------------
# 3. Binomial Probability
# ---------------------------------------------------------

"""
The binomial distribution is useful when:

1. There are a fixed number of trials.
2. Each trial has two possible outcomes.
3. The probability of success remains constant.
4. Trials are independent.

Formula:

P(X = k) = C(n,k) × p^k × (1-p)^(n-k)

where:

n = number of trials
k = number of successes
p = probability of success
"""


def binomial_probability(n, k, p):
    """
    Calculate the probability of obtaining exactly
    k successes in n independent trials.
    """

    combinations = math.comb(n, k)

    probability = (
        combinations
        * (p ** k)
        * ((1 - p) ** (n - k))
    )

    return probability


# Example:
# Suppose the probability of detecting a particular
# biological event in a sample is 0.3.

n = 10
k = 3
p = 0.3

binomial_result = binomial_probability(n, k, p)

print("\nBinomial Distribution")
print("---------------------")
print("Number of trials:", n)
print("Required successes:", k)
print("Probability of success:", p)
print("Probability of exactly 3 successes:",
      binomial_result)


# ---------------------------------------------------------
# 4. Normal Distribution
# ---------------------------------------------------------

"""
The normal distribution is a continuous probability
distribution with a bell-shaped curve.

Probability density function:

f(x) =
1 / (σ√(2π))
× exp[-(x-μ)^2 / (2σ^2)]

where:

μ = mean
σ = standard deviation
"""


def normal_probability_density(x, mean_value, standard_deviation):
    """
    Calculate the probability density of x
    for a normal distribution.
    """

    coefficient = 1 / (
        standard_deviation * math.sqrt(2 * math.pi)
    )

    exponent = -(
        (x - mean_value) ** 2
    ) / (
        2 * standard_deviation ** 2
    )

    density = coefficient * math.exp(exponent)

    return density


# Example biological measurement

mean_value = 100
standard_deviation = 15
measurement = 110

density = normal_probability_density(
    measurement,
    mean_value,
    standard_deviation
)

print("\nNormal Distribution")
print("-------------------")
print("Mean:", mean_value)
print("Standard deviation:", standard_deviation)
print("Measurement:", measurement)
print("Probability density:", density)


# ---------------------------------------------------------
# 5. Standard Score (Z-Score)
# ---------------------------------------------------------

"""
The z-score indicates how many standard deviations
an observation is away from the mean.

Formula:

z = (x - μ) / σ
"""

z_score = (
    measurement - mean_value
) / standard_deviation

print("\nZ-Score")
print("-------")
print("Measurement:", measurement)
print("Z-score:", z_score)


# ---------------------------------------------------------
# 6. Interpretation
# ---------------------------------------------------------

print("\nInterpretation")
print("--------------")

print(
    "A positive z-score means the observation is above "
    "the mean."
)

print(
    "A negative z-score means the observation is below "
    "the mean."
)

print(
    "The binomial distribution is useful for counting "
    "successes across a fixed number of independent trials."
)

print(
    "The normal distribution is commonly used to model "
    "continuous measurements under appropriate assumptions."
)


#File purpose
#Biological Data
      #↓
#Probability
      #↓
#Binomial Distribution
      #↓
#Normal Distribution
      #↓
#Z-Score
      #↓
#Statistical Interpretation
