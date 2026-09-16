"""
Correlation Analysis
--------------------

This script demonstrates basic correlation analysis
using biological measurements.

Topics:
- Pearson correlation
- Positive correlation
- Negative correlation
- Interpretation of correlation coefficient

Example:
Relationship between gene expression and disease score.
"""

import math


# ---------------------------------------------------------
# Example Biological Data
# ---------------------------------------------------------

# Gene-expression measurements

gene_expression = [
    2.1,
    3.2,
    4.0,
    5.1,
    6.3
]

# Corresponding disease scores

disease_score = [
    10,
    15,
    19,
    25,
    30
]


# ---------------------------------------------------------
# Check Dataset
# ---------------------------------------------------------

if len(gene_expression) != len(disease_score):
    raise ValueError(
        "Both datasets must contain the same number "
        "of observations."
    )


# ---------------------------------------------------------
# Calculate Means
# ---------------------------------------------------------

n = len(gene_expression)

mean_x = sum(gene_expression) / n
mean_y = sum(disease_score) / n


# ---------------------------------------------------------
# Calculate Pearson Correlation
# ---------------------------------------------------------

"""
Pearson correlation formula:

                 Σ[(x - x̄)(y - ȳ)]
r = ---------------------------------------------
    √[Σ(x - x̄)² × Σ(y - ȳ)²]

The result ranges from -1 to +1.
"""

numerator = 0
sum_x_squared = 0
sum_y_squared = 0

for x, y in zip(gene_expression, disease_score):

    deviation_x = x - mean_x
    deviation_y = y - mean_y

    numerator += deviation_x * deviation_y

    sum_x_squared += deviation_x ** 2
    sum_y_squared += deviation_y ** 2


denominator = math.sqrt(
    sum_x_squared * sum_y_squared
)


# ---------------------------------------------------------
# Handle Constant Data
# ---------------------------------------------------------

if denominator == 0:
    raise ValueError(
        "Correlation cannot be calculated when one "
        "variable has zero variance."
    )


correlation = numerator / denominator


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print("Correlation Analysis")
print("--------------------")

print("Gene expression:", gene_expression)
print("Disease score:", disease_score)

print("\nSample Information")
print("------------------")

print("Number of observations:", n)
print("Mean gene expression:", mean_x)
print("Mean disease score:", mean_y)

print("\nPearson Correlation")
print("-------------------")

print("Correlation coefficient (r):", correlation)


# ---------------------------------------------------------
# Interpret Direction
# ---------------------------------------------------------

print("\nInterpretation")
print("--------------")

if correlation > 0:
    print(
        "The variables show a positive linear association."
    )

elif correlation < 0:
    print(
        "The variables show a negative linear association."
    )

else:
    print(
        "The variables show no linear association."
    )


# ---------------------------------------------------------
# Interpret Approximate Strength
# ---------------------------------------------------------

absolute_r = abs(correlation)

if absolute_r >= 0.8:
    strength = "strong"

elif absolute_r >= 0.5:
    strength = "moderate"

elif absolute_r >= 0.3:
    strength = "weak"

else:
    strength = "very weak"


print(
    "Approximate strength of linear association:",
    strength
)


# ---------------------------------------------------------
# Important Reminder
# ---------------------------------------------------------

print("\nImportant")
print("---------")

print(
    "Correlation describes association between variables."
)

print(
    "Correlation does not by itself establish causation."
)
What this code covers
Gene Expression + Disease Score
            ↓
       Calculate Means
            ↓
    Pearson Correlation
            ↓
       Correlation r
            ↓
 Direction + Approximate Strength
