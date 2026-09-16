Introduction

Descriptive statistics provides methods for organizing, summarizing, and describing data. Before applying statistical tests or drawing biological conclusions, it is useful to understand the basic characteristics of the dataset.

Descriptive statistics can answer questions such as:

What is the typical value in the dataset?
How much variation is present?
What is the minimum and maximum value?
How are the observations distributed?
Measures of Central Tendency

Central tendency describes the typical or central value of a dataset.

Mean

The mean is calculated by adding all observations and dividing by the number of observations.

Mean = Sum of all observations / Number of observations

For example:

Data = 2, 4, 6, 8, 10

Mean = (2 + 4 + 6 + 8 + 10) / 5
     = 6

The mean can be strongly affected by extreme values.

Median

The median is the middle value after arranging observations in ascending or descending order.

For an odd number of observations:

2, 4, 6, 8, 10

Median = 6

For an even number of observations, the median is calculated from the two middle values.

2, 4, 6, 8

Median = (4 + 6) / 2
       = 5

The median is generally less affected by extreme values than the mean.

Mode

The mode is the value that occurs most frequently.

2, 3, 3, 4, 5, 3, 6

Mode = 3

A dataset can have:

One mode
More than one mode
No mode
Measures of Dispersion

Central tendency alone does not describe the complete dataset. Measures of dispersion describe how spread out the observations are.

Range

The range is the difference between the largest and smallest observations.

Range = Maximum − Minimum

For:

5, 8, 10, 12, 17
Range = 17 − 5
      = 12
Variance

Variance measures the average squared deviation of observations from the mean.

A larger variance indicates greater spread around the mean.

For a population:

σ² = Σ(x − μ)² / N

For a sample:

s² = Σ(x − x̄)² / (n − 1)

where:

x = individual observation
μ = population mean
x̄ = sample mean
N = population size
n = sample size
Standard Deviation

Standard deviation is the square root of variance.

Standard Deviation = √Variance

It provides a measure of how much observations typically vary around the mean.

For example:

Dataset A → Mean = 50, SD = 2
Dataset B → Mean = 50, SD = 15

Both datasets have the same mean, but Dataset B has considerably greater variability.

Quartiles

Quartiles divide ordered data into four sections.

The main quartiles are:

Q1 → First quartile
Q2 → Second quartile / median
Q3 → Third quartile

Conceptually:

Minimum ─── Q1 ─── Q2 ─── Q3 ─── Maximum
             │      │      │
            25%    50%    75%
Interquartile Range

The interquartile range (IQR) measures the spread of the middle 50% of observations.

IQR = Q3 − Q1

The IQR is less influenced by extreme observations than the full range.

Outliers

An outlier is an observation that is unusually distant from the rest of the dataset.

One commonly used IQR-based approach identifies potential outliers using:

Lower limit = Q1 − 1.5 × IQR

Upper limit = Q3 + 1.5 × IQR

Observations outside these limits may be considered potential outliers.

However, an outlier should not automatically be removed. It may represent:

Genuine biological variation
Experimental variation
Measurement error
Data-entry error
An unusual biological condition

The reason for an observation being unusual should be investigated before deciding how to handle it.

Example Biological Dataset

Consider the following measurements:

12, 15, 14, 18, 16, 15, 13, 20, 17, 15

Descriptive statistics could be used to determine:

Mean
Median
Mode
Minimum
Maximum
Range
Variance
Standard Deviation
Quartiles
IQR

These values provide an initial summary before further statistical analysis.

Descriptive Statistics in Bioinformatics

Descriptive statistics are useful in many biological datasets.

Examples include:

Gene-expression measurements
Protein concentrations
Cell counts
Enzyme activity
Clinical measurements
Growth measurements
Experimental assay results

For example, gene-expression data may contain measurements from multiple biological samples:

Sample 1 → Expression value
Sample 2 → Expression value
Sample 3 → Expression value
       ↓
Descriptive Statistics
       ↓
Mean + Variability

This provides an initial understanding of the dataset before differential or inferential analysis.

Visualization

Descriptive statistics are often combined with visualizations.

Common plots include:

Histograms
Box plots
Bar charts
Scatter plots

For example, a box plot can display:

       Maximum
          │
       ┌──┴──┐
       │     │
   Q3 ─┤─────├
       │  │  │
   Q2 ─┤─────├  Median
       │  │  │
   Q1 ─┤─────├
       │     │
       └──┬──┘
          │
       Minimum

Visualization can reveal patterns that may not be obvious from numerical summaries alone.

Mean vs Median
Feature	Mean	Median
Calculation	Average of observations	Middle observation
Effect of outliers	More affected	Less affected
Useful for	Approximately symmetric data	Skewed data
Requires ordering	No	Yes
Important Distinction

Descriptive statistics describe the observed dataset.

They do not by themselves establish:

Causation
Statistical significance
Biological mechanism
Generalization to a wider population

Those questions require appropriate inferential or biological analysis.

Quick Revision
Descriptive Statistics

Central Tendency
├── Mean
├── Median
└── Mode

Dispersion
├── Range
├── Variance
├── Standard Deviation
└── IQR

Distribution
├── Quartiles
└── Outliers
Conclusion

Descriptive statistics is the first step toward understanding a dataset. Measures such as mean, median, mode, range, variance, standard deviation, quartiles, and IQR summarize the central tendency and variability of observations.

In bioinformatics, these basic summaries provide an important foundation for understanding biological datasets before proceeding to statistical testing and more advanced analyses.
