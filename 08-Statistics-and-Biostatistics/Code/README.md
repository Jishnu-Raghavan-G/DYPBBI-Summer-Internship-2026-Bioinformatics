# Statistics and Biostatistics Code

This folder contains Python scripts demonstrating basic statistical concepts used in biological and bioinformatics data analysis.

## Code Files

### `Descriptive-Statistics.py`

Demonstrates basic descriptive statistics for biological measurements.

Topics covered:

- Mean
- Median
- Mode
- Minimum
- Maximum
- Range
- Variance
- Standard deviation

Basic workflow:

```text
Biological Data
      ↓
Descriptive Statistics
      ↓
Mean / Median / Mode
      ↓
Range / Variance
      ↓
Standard Deviation
Probability-and-Distributions.py

Demonstrates basic probability concepts and probability distributions.

Topics covered:

Basic probability
Complementary probability
Binomial distribution
Normal distribution
Z-score

The script includes examples using biological measurements and events.

Basic workflow:

Biological Event
      ↓
Probability
      ↓
Probability Distribution
      ↓
Statistical Interpretation
Hypothesis-Testing.py

Demonstrates the basic workflow of hypothesis testing using a one-sample t-statistic.

Topics covered:

Null hypothesis
Alternative hypothesis
Sample mean
Sample standard deviation
Standard error
t-statistic
Significance level

Basic workflow:

Biological Data
      ↓
H₀ and H₁
      ↓
Sample Statistics
      ↓
Standard Error
      ↓
t-statistic
      ↓
Statistical Interpretation
Correlation-Analysis.py

Demonstrates Pearson correlation using two biological variables.

Example:

Gene Expression
       ↕
Disease Score

Topics covered:

Mean calculation
Pearson correlation coefficient
Positive correlation
Negative correlation
Correlation strength
Interpretation

Basic workflow:

Two Biological Variables
        ↓
Calculate Means
        ↓
Calculate Pearson r
        ↓
Determine Direction
        ↓
Interpret Association
Requirements

The scripts are designed to use Python's standard library wherever possible.

For the basic scripts, no external installation is required.

Python 3.x is recommended.

Running the Scripts

From the Code directory:

python Descriptive-Statistics.py
python Probability-and-Distributions.py
python Hypothesis-Testing.py
python Correlation-Analysis.py
Important Notes

These scripts are primarily educational examples designed to demonstrate statistical concepts.

The example datasets are illustrative and should not be interpreted as actual experimental results.

For real biological datasets, statistical methods should be selected according to:

Experimental design
Data type
Sample size
Distribution
Independence of observations
Biological context
Multiple-testing requirements
Reproducibility

Keeping statistical calculations in scripts makes the analysis easier to understand and reproduce.

A basic reproducible workflow is:

Input Data
    ↓
Python Script
    ↓
Statistical Analysis
    ↓
Output
    ↓
Interpretation
Section Summary

The scripts in this folder provide a foundation for understanding how statistical concepts can be implemented computationally.

The progression is:

Descriptive Statistics
        ↓
Probability and Distributions
        ↓
Hypothesis Testing
        ↓
Correlation Analysis
        ↓
Biological Data Interpretation
