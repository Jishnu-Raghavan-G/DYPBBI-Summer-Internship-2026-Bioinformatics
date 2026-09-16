Overview

This section introduces the statistical concepts required for working with biological and bioinformatics datasets.

Statistics is an important part of bioinformatics because biological datasets often contain variation, uncertainty, repeated measurements, and large numbers of observations. Statistical methods help organize this information and determine whether observed patterns may be meaningful.

The topics covered here range from basic descriptive statistics and probability to hypothesis testing, confidence intervals, correlation, and biological-data analysis.

Topics Covered
08-Statistics-and-Biostatistics/
│
├── README.md
├── Descriptive-Statistics.md
├── Data-Distribution.md
├── Probability.md
├── Hypothesis-Testing.md
├── P-Values.md
├── Confidence-Intervals.md
├── Correlation.md
├── Biological-Data-Analysis.md
│
└── Code/
    ├── Descriptive-Statistics.py
    ├── Probability-and-Distributions.py
    ├── Hypothesis-Testing.py
    ├── Correlation-Analysis.py
    └── README.md
Descriptive Statistics

Descriptive statistics are used to summarize and describe datasets.

Important measures include:

Mean
Median
Mode
Range
Variance
Standard deviation
Quartiles
Interquartile range

These measures provide an initial understanding of a dataset before more advanced statistical analysis is performed.

Data Distribution

Understanding how biological observations are distributed is important for selecting appropriate statistical methods.

Topics include:

Frequency distributions
Normal distribution
Variability
Standard deviation
Skewness
Outliers
Distribution of biological measurements

A dataset's distribution can influence the choice of statistical test.

Probability

Probability provides a mathematical framework for describing uncertainty.

Basic concepts include:

Probability of an event
Independent events
Conditional probability
Probability distributions
Random variables

Probability concepts are fundamental to many statistical methods used in biological-data analysis.

Hypothesis Testing

Hypothesis testing provides a framework for evaluating statistical evidence.

A simplified workflow is:

Research Question
      ↓
Null Hypothesis
      ↓
Alternative Hypothesis
      ↓
Select Statistical Test
      ↓
Calculate Test Statistic
      ↓
Determine P-value
      ↓
Interpret Evidence

The statistical conclusion should be based on the predefined significance level and the assumptions of the selected test.

P-Values

A p-value is used to quantify how compatible the observed data are with a specified null hypothesis.

It is important to remember that a p-value is not:

The probability that the null hypothesis is true
A measure of biological importance
A measure of the size of an effect

Statistical significance and biological significance are different concepts.

Confidence Intervals

A confidence interval provides a range of values associated with an estimated parameter under a specified statistical procedure.

It can provide information about the uncertainty around an estimate rather than reporting only a single value.

For biological data, confidence intervals can be useful when interpreting measurements such as:

Means
Differences between groups
Correlations
Other estimated parameters
Correlation

Correlation describes the degree to which two variables are associated.

For example:

Gene Expression
      ↕
Clinical Measurement

Correlation analysis can help identify relationships between variables, although correlation does not by itself establish causation.

Common correlation measures include:

Pearson correlation
Spearman rank correlation
Biological Data Analysis

Statistical analysis is widely used in bioinformatics and computational biology.

Examples include:

Gene-expression analysis
Comparing healthy and disease groups
Identifying differentially expressed genes
Evaluating experimental measurements
Studying relationships between biological variables
Assessing uncertainty in biological observations

In the asthma transcriptomics case study, statistical filtering was used after GEO2R analysis to identify genes for downstream functional and network analysis.

Python and Statistical Analysis

The Code/ directory contains simple Python examples demonstrating statistical calculations and data analysis.

Biological Dataset
       ↓
Python
       ↓
Statistical Calculation
       ↓
Summary / Test
       ↓
Interpretation

The scripts are intended to connect statistical concepts with practical computational analysis.

Learning Workflow
Descriptive Statistics
        ↓
Data Distribution
        ↓
Probability
        ↓
Hypothesis Testing
        ↓
P-values
        ↓
Confidence Intervals
        ↓
Correlation
        ↓
Biological Data Analysis

This progression moves from basic data description toward statistical interpretation of biological datasets.

Important Considerations

Statistical analysis should always consider:

Sample size
Data distribution
Experimental design
Independence of observations
Appropriate statistical test
Test assumptions
Multiple testing where applicable
Effect size
Biological relevance

A statistically significant result should therefore be interpreted in the context of the underlying biological question.

Conclusion

Statistics provides the foundation for reliable interpretation of biological data. The concepts in this section build from describing datasets to evaluating statistical evidence and relationships between variables.

Understanding these principles is particularly important in bioinformatics workflows involving gene-expression datasets, differential-expression analysis, and downstream biological interpretation.
