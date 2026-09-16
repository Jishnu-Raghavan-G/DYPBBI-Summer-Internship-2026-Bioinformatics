# Biostatistics Workshop

## Introduction

Biostatistics is the application of statistical methods to biological, medical, and life-science data.

Biological experiments and computational analyses often produce variable and uncertain measurements. Statistical methods provide a systematic way to summarize these observations, identify patterns, compare groups, and evaluate whether observed differences may be meaningful.

The biostatistics workshop provided additional exposure to the role of statistics in biological research and complemented the statistical concepts covered during the internship.

---

## Role of Statistics in Biological Research

Statistics can be used throughout a research workflow:

```text
Research Question
       ↓
Data Collection
       ↓
Data Organization
       ↓
Descriptive Statistics
       ↓
Statistical Analysis
       ↓
Interpretation
       ↓
Scientific Conclusion

Statistical analysis helps researchers convert biological observations into interpretable evidence.

Types of Biological Data

Biological datasets can contain different types of variables.

Quantitative Data

Quantitative data are numerical measurements.

Examples include:

Height
Weight
Cell concentration
Protein concentration
Gene-expression values
Blood glucose level
Qualitative Data

Qualitative or categorical data describe categories or groups.

Examples include:

Healthy / Disease
Male / Female
Treatment / Control
Positive / Negative
Descriptive Statistics

Descriptive statistics summarize the characteristics of a dataset.

Important measures include:

Mean
Median
Mode
Range
Variance
Standard deviation
Percentiles
Mean

The arithmetic mean is calculated by adding all observations and dividing by the number of observations.

Mean = Sum of observations / Number of observations

For example:

Data = 2, 4, 6, 8

Mean = (2 + 4 + 6 + 8) / 4
     = 5
Median

The median is the middle value after the observations are arranged in ascending or descending order.

For an odd number of observations, it is the central value.

For an even number of observations, it is the average of the two central values.

Mode

The mode is the value that occurs most frequently in a dataset.

Example:

Data = 2, 3, 3, 4, 5

Mode = 3
Range

The range represents the difference between the maximum and minimum observations.

Range = Maximum value - Minimum value

A larger range indicates greater spread between the extreme observations.

Variance

Variance measures the dispersion of observations around the mean.

A larger variance indicates greater variability within the dataset.

Standard Deviation

Standard deviation describes the typical spread of observations around the mean.

A smaller standard deviation indicates that observations tend to be closer to the mean.

A larger standard deviation indicates greater variability.

Data Distribution

The distribution of data describes how observations are spread across possible values.

Common distributions encountered in statistical analysis include:

Normal distribution
Binomial distribution
Poisson distribution

Understanding the distribution of data can help determine which statistical methods are appropriate.

Normal Distribution

The normal distribution is a continuous probability distribution with a characteristic bell-shaped curve.

Important properties include:

Symmetry around the mean
Mean, median, and mode coincide in an ideal normal distribution
Most observations occur near the mean
Fewer observations occur farther from the mean

Normal distributions are commonly encountered in biological measurements and statistical models.

Probability

Probability describes the likelihood of an event occurring.

It ranges from:

0 ≤ P(Event) ≤ 1

where:

P(Event) = 0

represents an impossible event, while:

P(Event) = 1

represents a certain event.

Hypothesis Testing

Hypothesis testing provides a framework for evaluating claims about a population using sample data.

The two main hypotheses are:

Null Hypothesis

The null hypothesis generally represents the absence of a specified difference or effect.

Alternative Hypothesis

The alternative hypothesis represents the presence of a difference or effect being investigated.

A simplified workflow is:

Define Hypotheses
       ↓
Collect Data
       ↓
Select Statistical Test
       ↓
Calculate Test Statistic
       ↓
Determine p-value
       ↓
Interpret the Result
P-Value

A p-value is used in hypothesis testing to evaluate how compatible the observed data are with the null hypothesis under the statistical model.

A commonly used significance threshold is:

α = 0.05

However, statistical significance should not be interpreted solely from whether a p-value crosses a threshold. The research question, effect size, study design, assumptions, and biological relevance should also be considered.

Confidence Intervals

A confidence interval provides a range of values associated with an estimated parameter under a specified confidence procedure.

For example, a 95% confidence interval provides a range calculated using a method designed to have 95% coverage in repeated sampling under the relevant assumptions.

Confidence intervals can provide information about both the estimated value and its uncertainty.

Correlation

Correlation measures the strength and direction of association between variables.

A commonly used measure is Pearson's correlation coefficient.

Its value ranges from:

-1 ≤ r ≤ +1

Interpretation:

r > 0  → Positive association
r < 0  → Negative association
r ≈ 0  → Little or no linear association

The magnitude of r indicates the strength of a linear relationship.

Correlation Does Not Imply Causation

A correlation between two variables does not by itself demonstrate that one variable causes the other.

For example, two biological variables may be correlated because:

One influences the other
Both are influenced by another variable
The relationship is coincidental
The data or study design introduces confounding

Causal conclusions require appropriate study designs and additional evidence.

Statistics in Transcriptomics

Statistical analysis is particularly important in transcriptomics because gene-expression datasets can contain measurements for thousands of genes.

A simplified workflow is:

Gene-Expression Dataset
        ↓
Sample Groups
        ↓
Statistical Comparison
        ↓
Differential Gene Expression
        ↓
Multiple-Testing Consideration
        ↓
Candidate Gene Selection
        ↓
Biological Interpretation

The internship included differential gene-expression analysis and statistical filtering using measures such as log2 fold change and adjusted p-values.

Multiple Testing

In high-dimensional biological datasets, many statistical tests may be performed simultaneously.

For example, if thousands of genes are tested independently, some may appear statistically significant simply by chance.

Multiple-testing correction helps control this problem.

One commonly used measure is the adjusted p-value.

Biological Significance vs Statistical Significance

Statistical significance and biological importance are not identical.

A statistically significant result may have a very small effect size.

Conversely, a biologically interesting effect may not reach statistical significance because of:

Small sample size
High variability
Experimental limitations
Insufficient statistical power

Therefore, biological interpretation should consider both statistical evidence and biological context.

Biostatistics in the Internship

Statistical concepts formed part of the broader bioinformatics training.

The internship covered biological data analysis alongside transcriptomics, differential expression, functional analysis, and computational interpretation.

The statistical concepts were relevant to interpreting biological datasets and evaluating differences between experimental or biological groups.

Practical Applications

Biostatistics can be applied to:

Gene-expression analysis
Clinical research
Epidemiology
Population studies
Drug-development studies
Experimental biology
Genomics
Proteomics
Microbiology
Bioprocessing
Example Biological Workflow

Consider an experiment comparing two biological groups:

Control Group
      +
Treatment Group
      ↓
Data Collection
      ↓
Descriptive Statistics
      ↓
Statistical Test
      ↓
p-value / Confidence Interval
      ↓
Interpretation

The statistical method should be selected according to the study design, variable type, distribution, assumptions, and research question.

Good Statistical Practice

A biological analysis should:

Define the research question clearly
Identify the variables
Understand the study design
Inspect the data before testing
Select an appropriate statistical method
Check relevant assumptions
Consider sample size
Account for multiple testing when necessary
Report effect sizes where appropriate
Report uncertainty
Interpret results in biological context
Common Statistical Mistakes
Treating Every p-value as Proof

A p-value does not by itself establish biological importance or causality.

Ignoring Sample Size

Statistical results can be strongly affected by the number of observations.

Ignoring Data Distribution

Some statistical methods rely on assumptions about the underlying data.

Confusing Correlation with Causation

Association alone does not demonstrate a causal relationship.

Ignoring Multiple Testing

Testing many hypotheses without appropriate correction can increase false-positive findings.

Reporting Only Significant Results

Focusing exclusively on statistically significant findings can give an incomplete picture of the data.

Connection to Computational Biology

Computational biology frequently involves large datasets.

Statistics provides the framework for:

Data
 ↓
Pattern Identification
 ↓
Quantitative Comparison
 ↓
Uncertainty Assessment
 ↓
Biological Interpretation

Therefore, statistical literacy is an important component of bioinformatics and computational biology.

Key Takeaways
Biostatistics applies statistical methods to biological data.
Descriptive statistics summarize datasets.
Probability provides a mathematical framework for uncertainty.
Hypothesis testing helps evaluate statistical evidence for differences or effects.
P-values should be interpreted in context rather than treated as standalone measures of importance.
Confidence intervals communicate estimates together with uncertainty.
Correlation describes association but does not establish causation.
Multiple testing is particularly important in high-dimensional biological datasets.
Statistical significance and biological significance are different concepts.
Appropriate statistical analysis is essential for reliable interpretation of biological and bioinformatics data.
