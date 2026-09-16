"""
Hypothesis Testing
------------------

This script demonstrates the basic idea of hypothesis testing.

Topics:
- Null hypothesis (H0)
- Alternative hypothesis (H1)
- Sample mean
- One-sample t-test
- Test statistic
- p-value
- Significance level

Example:
Testing whether the mean of a biological measurement
is significantly different from a hypothesized value.
"""

import math


# ---------------------------------------------------------
# Example Biological Data
# ---------------------------------------------------------

# Example measurements from biological samples

data = [12, 14, 15, 13, 16, 14, 15, 17, 13, 16]

# Hypothesized population mean

hypothesized_mean = 12

# Significance level

alpha = 0.05


# ---------------------------------------------------------
# Basic Calculations
# ---------------------------------------------------------

n = len(data)

sample_mean = sum(data) / n

# Sample variance

squared_deviations = [
    (x - sample_mean) ** 2
    for x in data
]

sample_variance = (
    sum(squared_deviations) / (n - 1)
)

sample_standard_deviation = math.sqrt(
    sample_variance
)

# Standard error

standard_error = (
    sample_standard_deviation / math.sqrt(n)
)


# ---------------------------------------------------------
# One-Sample t-Test Statistic
# ---------------------------------------------------------

"""
Formula:

t = (x̄ - μ0) / (s / √n)

where:

x̄  = sample mean
μ0 = hypothesized population mean
s  = sample standard deviation
n  = sample size
"""

t_statistic = (
    sample_mean - hypothesized_mean
) / standard_error


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print("Hypothesis Testing")
print("------------------")

print("Data:", data)
print("Sample size:", n)
print("Sample mean:", sample_mean)
print("Sample standard deviation:",
      sample_standard_deviation)
print("Standard error:", standard_error)

print("\nHypothesized Mean")
print("-----------------")
print("H0 mean:", hypothesized_mean)

print("\nTest Statistic")
print("--------------")
print("t-statistic:", t_statistic)


# ---------------------------------------------------------
# Hypotheses
# ---------------------------------------------------------

print("\nHypotheses")
print("----------")

print(
    "H0: The population mean is equal to the "
    "hypothesized mean."
)

print(
    "H1: The population mean is different from "
    "the hypothesized mean."
)


# ---------------------------------------------------------
# Interpretation
# ---------------------------------------------------------

print("\nInterpretation")
print("--------------")

print(
    "The calculated t-statistic measures how far the "
    "sample mean is from the hypothesized mean relative "
    "to the estimated standard error."
)

print(
    "A complete hypothesis test should compare the "
    "test statistic with the appropriate critical value "
    "or calculate the corresponding p-value."
)

print(
    "The significance level used in this example is:",
    alpha
)
Important note

This script calculates the one-sample t-statistic, but deliberately does not hard-code a p-value or critical value. Those depend on the degrees of freedom (n - 1) and whether the test is one-tailed or two-tailed.

For the complete version, we can use scipy.stats to calculate the actual p-value.

Workflow
Biological Data
      ↓
Define H₀ and H₁
      ↓
Calculate Sample Mean
      ↓
Calculate Standard Deviation
      ↓
Calculate Standard Error
      ↓
Calculate Test Statistic
      ↓
Calculate p-value
      ↓
Compare with α
      ↓
Interpret Results
