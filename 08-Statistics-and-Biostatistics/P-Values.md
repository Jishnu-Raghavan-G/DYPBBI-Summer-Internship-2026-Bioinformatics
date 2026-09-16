Introduction

A p-value is a statistical quantity used in hypothesis testing to describe how compatible the observed data are with a specified null hypothesis.

It is commonly used when determining whether an observed difference or association provides sufficient statistical evidence against the null hypothesis.

Basic Idea

The general relationship is:

Null Hypothesis (H₀)
        ↓
Collect / Analyze Data
        ↓
Statistical Test
        ↓
Calculate Test Statistic
        ↓
Calculate P-value
        ↓
Interpret Evidence Against H₀

A smaller p-value indicates that the observed data would be less compatible with the null hypothesis under the assumptions of the statistical test.

Significance Level

Before interpreting a p-value, a significance level α is generally specified.

A commonly used value is:

α = 0.05

The decision framework is:

p-value ≤ α
      ↓
Reject H₀

p-value > α
      ↓
Fail to reject H₀

For example:

α = 0.05
p = 0.02

0.02 < 0.05
      ↓
Reject H₀

This means the result meets the predefined statistical significance criterion.

What a P-value Means

A p-value can be understood as a measure of how unusual the observed result would be, or something more extreme, assuming the null hypothesis and the statistical model are correct.

It does not directly tell us the probability that the null hypothesis is true.

What a P-value Does Not Mean

A p-value is not:

The probability that the null hypothesis is true
The probability that the alternative hypothesis is true
The probability that the result occurred "by chance"
A measure of effect size
A measure of biological importance

For example:

p = 0.01

does not mean:

"There is a 1% probability that H₀ is true."

That is not the correct interpretation.

P-value and Statistical Significance

A result is commonly called statistically significant when:

p-value ≤ predefined α

For example:

P-value	α	Statistical interpretation
0.001	0.05	Meets significance criterion
0.02	0.05	Meets significance criterion
0.05	0.05	Meets criterion if the stated rule is ≤
0.18	0.05	Does not meet criterion

The exact interpretation should always be connected to the predefined statistical procedure and significance level.

Statistical Significance vs Effect Size

A p-value does not indicate how large an effect is.

Consider:

Study A:
Small effect + large sample
       ↓
Small p-value possible

Study B:
Large effect + small sample
       ↓
Larger p-value possible

Therefore, statistical significance should be considered alongside measures such as:

Effect size
Confidence intervals
Sample size
Biological context
P-values in Biological Research

P-values are commonly encountered when comparing biological groups.

For example:

Healthy Samples
       │
       │
       ├── Statistical Test ──→ P-value
       │
       │
Disease Samples

The p-value can help determine whether the observed difference is statistically supported under the specified hypothesis-testing framework.

P-values in Transcriptomics

Transcriptomics can involve testing thousands of genes simultaneously.

For example:

Gene 1     → p-value
Gene 2     → p-value
Gene 3     → p-value
   .
   .
   .
Gene 20,000 → p-value

If each gene is evaluated independently using an unadjusted threshold, some apparently small p-values can arise simply because a very large number of tests were performed.

Therefore, transcriptomics commonly uses multiple-testing correction.

In the DYPBBI asthma transcriptomics workflow, statistical filtering was applied to the GEO2R results before selected genes were taken forward for functional and network analyses.

Adjusted P-values

An adjusted p-value accounts for the fact that multiple statistical tests have been performed.

One commonly encountered approach is controlling the False Discovery Rate (FDR).

Conceptually:

Raw Gene-Expression Data
        ↓
Statistical Testing
        ↓
Many Raw P-values
        ↓
Multiple-Testing Correction
        ↓
Adjusted P-values
        ↓
Statistical Filtering

Adjusted p-values are particularly important in high-throughput bioinformatics analyses.

P-value and Confidence Interval

P-values and confidence intervals provide different types of information.

P-value
   ↓
Evidence against H₀

Confidence Interval
   ↓
Range associated with an estimated parameter

Using both can provide a more informative statistical interpretation than relying on a p-value alone.

Example: Gene-Expression Comparison

Suppose an analysis compares gene expression between healthy and disease groups.

The analysis produces:

Gene X

p-value = 0.003
α = 0.05

Since:

0.003 < 0.05

the result meets the chosen significance criterion.

However, additional questions remain:

How large is the expression difference?
What is the effect size?
What is the confidence interval?
Was this one of many genes tested?
Was multiple-testing correction performed?
Is the difference biologically meaningful?

These questions are essential for proper interpretation.

Common Misinterpretations
"A Smaller P-value Means a Larger Effect"

Not necessarily.

The p-value depends on factors including the observed effect, variability, sample size, and statistical model.

"P > 0.05 Proves There Is No Effect"

Not necessarily.

Failing to reject the null hypothesis means the analysis did not provide sufficient statistical evidence against it at the chosen significance level. It does not prove that the effect is exactly zero.

"P < 0.05 Proves the Hypothesis Is True"

No.

It means the result meets the predefined statistical criterion for rejecting the null hypothesis under the specified testing framework.

Quick Revision
P-value
   ↓
Assume H₀
   ↓
Ask how compatible the observed data
are with H₀
   ↓
Compare p with α
Key Points
A p-value is used in hypothesis testing.
It is interpreted relative to a predefined significance level.
A small p-value provides stronger evidence against H₀ under the model assumptions.
It does not give the probability that H₀ is true.
It does not measure biological importance.
Effect size and confidence intervals provide additional information.
Multiple testing must be considered in high-throughput bioinformatics.
Conclusion

The p-value is an important component of statistical inference, but it should not be interpreted in isolation. Proper analysis requires consideration of the null hypothesis, significance level, effect size, confidence intervals, sample size, multiple testing, and biological context.

In bioinformatics, particularly in transcriptomics, this broader interpretation is essential because thousands of statistical tests may be performed simultaneously.
