Introduction

Data distribution describes how values are spread across a dataset. Understanding the distribution of biological measurements is important because it helps determine the characteristics of the data and can influence which statistical methods are appropriate.

For example, measurements from biological experiments may cluster around a central value, show considerable variation, or contain unusually high or low observations.

Frequency Distribution

A frequency distribution shows how often different values or ranges of values occur.

For example:

Measurement Range    Frequency

0–10                    2
10–20                   5
20–30                   8
30–40                   4
40–50                   1

This makes it easier to see where observations are concentrated.

Histogram

A histogram represents the frequency distribution of continuous numerical data.

Frequency
   │
   │        ███
   │      ███████
   │    ███████████
   │  █████████████
   │____________________
       Measurement

The shape of a histogram can provide information about:

Central tendency
Spread
Skewness
Possible outliers
Overall distribution pattern
Normal Distribution

The normal distribution is a commonly encountered probability distribution characterized by a symmetric, bell-shaped curve.

Frequency
   │
   │             █
   │           ████
   │         ███████
   │       ███████████
   │     █████████████
   │________________________
              Mean

In an ideal normal distribution:

Mean = Median = Mode

The distribution is symmetric around its mean.

Standard Deviation and Distribution

Standard deviation describes the spread of observations around the mean.

For a normally distributed dataset, approximately:

Mean ± 1 SD → ~68% of observations

Mean ± 2 SD → ~95% of observations

Mean ± 3 SD → ~99.7% of observations

This relationship is commonly referred to as the 68–95–99.7 rule.

Skewness

A distribution is skewed when it is not symmetric.

Right-Skewed Distribution

A right-skewed distribution has a longer tail toward larger values.

Frequency
   │
   │     ████
   │   ███████
   │ █████████
   │███████████
   │________________________→
                         Tail

Large values extend the distribution toward the right.

Left-Skewed Distribution

A left-skewed distribution has a longer tail toward smaller values.

Frequency
   │
   │             ████
   │           ███████
   │         █████████
   │       ███████████
   │←____________________
     Tail
Mean and Skewness

In a skewed distribution, the mean can be pulled toward the longer tail.

For a typical right-skewed distribution:

Mode < Median < Mean

For a typical left-skewed distribution:

Mean < Median < Mode

These relationships are general patterns rather than universal rules.

Outliers

An outlier is an observation that is unusually distant from other observations.

For example:

12  13  14  15  15  16  17  18  45
                                ↑
                             Outlier

Outliers can substantially affect measures such as:

Mean
Variance
Standard deviation
Correlation

They should therefore be investigated rather than automatically deleted.

Box Plot

A box plot provides a compact representation of the distribution of numerical data.

It commonly displays:

Minimum
Q1
Median
Q3
Maximum
Potential outliers
       │
       │
   ┌───┴───┐
   │       │
   │   ────│  Median
   │       │
   └───┬───┘
       │
       │

The interquartile range is:

IQR = Q3 − Q1
Population and Sample

A population refers to the complete group of observations of interest.

A sample is a subset taken from that population.

Population
┌───────────────────────────┐
│ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ │
│ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ │
└───────────────────────────┘
             ↓
          Sample
       ┌───────────┐
       │ ○ ○ ○ ○ ○ │
       └───────────┘

Statistical analysis often uses a sample to make inferences about a larger population.

Distribution of Biological Data

Biological measurements can have different distributions depending on the variable and experimental system.

Examples include:

Gene-expression values
Protein concentrations
Cell counts
Enzyme activity
Clinical measurements
Growth measurements

There is no requirement that every biological dataset follow a normal distribution.

Why Distribution Matters

The distribution of data can influence:

Choice of statistical test
Summary statistics
Interpretation of variability
Identification of outliers
Data transformation
Visualization methods

A simplified workflow is:

Biological Dataset
       ↓
Visualize Data
       ↓
Examine Distribution
       ↓
Check Variability / Outliers
       ↓
Select Appropriate Statistical Approach
Normality

Normality refers to whether data are reasonably consistent with a normal distribution.

Normality can be explored using:

Histograms
Q–Q plots
Box plots
Statistical normality tests

A normality test should not be treated as the only basis for deciding how to analyze data. Sample size, study design, biological context, and robustness of the intended method should also be considered.

Data Transformation

Sometimes a transformation is used to make a distribution more suitable for analysis.

Common transformations include:

Log transformation
Square-root transformation
Other appropriate mathematical transformations

For example:

Highly skewed data
       ↓
Log transformation
       ↓
More symmetric representation
       ↓
Further analysis

Whether a transformation is appropriate depends on the dataset and research question.

Quick Revision
Data Distribution
│
├── Frequency Distribution
├── Histogram
├── Normal Distribution
├── Skewness
├── Outliers
├── Box Plot
├── Quartiles
└── IQR
Key Points
Distribution describes how observations are spread.
A normal distribution is symmetric and bell-shaped.
Skewed distributions have asymmetric tails.
Outliers can strongly influence statistical summaries.
Histograms and box plots help visualize distributions.
Distribution should be considered before selecting statistical methods.
Conclusion

Understanding data distribution is an essential step in statistical analysis. Examining shape, spread, skewness, and outliers helps researchers understand biological datasets before applying statistical tests.

In bioinformatics, this is particularly important because biological datasets can contain substantial variability and may not always follow simple theoretical distributions.
