"""
Descriptive Statistics
----------------------

Basic descriptive statistical analysis of biological data.

This script demonstrates:
- Mean
- Median
- Mode
- Minimum
- Maximum
- Range
- Variance
- Standard deviation

The example dataset represents a simple set of biological measurements.
"""

from statistics import mean, median, mode, variance, stdev


# ---------------------------------------------------------
# Example Biological Data
# ---------------------------------------------------------

data = [12, 15, 14, 18, 20, 15, 17, 13, 16, 15]


# ---------------------------------------------------------
# Basic Descriptive Statistics
# ---------------------------------------------------------

data_mean = mean(data)
data_median = median(data)
data_mode = mode(data)

minimum = min(data)
maximum = max(data)

data_range = maximum - minimum

data_variance = variance(data)
data_standard_deviation = stdev(data)


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print("Biological Data")
print("----------------")
print(data)

print("\nDescriptive Statistics")
print("----------------------")

print("Mean:", data_mean)
print("Median:", data_median)
print("Mode:", data_mode)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Range:", data_range)
print("Variance:", data_variance)
print("Standard Deviation:", data_standard_deviation)


# ---------------------------------------------------------
# Simple Interpretation
# ---------------------------------------------------------

print("\nInterpretation")
print("--------------")
print("The mean represents the average value of the dataset.")
print("The median represents the middle value.")
print("The mode represents the most frequently occurring value.")
print("The standard deviation describes the spread of the observations.")
What this file demonstrates
Biological Data
      ↓
Mean
Median
Mode
      ↓
Minimum / Maximum
      ↓
Range
      ↓
Variance
      ↓
Standard Deviation
