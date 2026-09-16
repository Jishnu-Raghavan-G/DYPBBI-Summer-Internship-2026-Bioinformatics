# Confidence Intervals

Confidence intervals are used to estimate an unknown population parameter from sample data.

Instead of reporting only a single estimate, a confidence interval provides a range of plausible values for the population parameter.

## 1. Basic Idea

Suppose we measure the expression level of a gene in a sample.

The sample gives us a sample mean, but the true population mean is unknown.

A confidence interval provides a range of values for the unknown population parameter based on the sample.

```text
Sample Data
    ↓
Calculate Estimate
    ↓
Calculate Uncertainty
    ↓
Confidence Interval
    ↓
Range of Plausible Population Values
2. Important Terms
Population

The complete group being studied.

Examples:

All patients with a particular disease
All individuals in a population
All biological samples belonging to a study population
Sample

A smaller group selected from the population.

Population
    ↓
Sample
    ↓
Statistical Analysis
Parameter

A numerical characteristic of a population.

Examples:

Population mean
Population proportion
Population standard deviation
Statistic

A numerical value calculated from a sample.

Examples:

Sample mean
Sample proportion
Sample standard deviation
3. Confidence Level

Common confidence levels include:

90%
95%
99%

A 95% confidence level is commonly used in scientific and biomedical research.

The confidence level refers to the long-run performance of the interval-generating procedure over repeated samples.

It should not be interpreted as saying that there is a 95% probability that a particular fixed population parameter lies inside an already-calculated interval.

4. General Formula

The general structure is:

Confidence Interval
= Estimate ± Margin of Error

For a population mean:

CI = x̄ ± Critical Value × Standard Error

where:

x̄ = sample mean
Critical Value = value determined by the confidence level and statistical distribution
Standard Error = uncertainty associated with the estimate
5. Standard Error

Standard error describes the variability of a sample statistic across repeated samples.

For a sample mean:

SE = s / √n

where:

s = sample standard deviation
n = sample size

As sample size increases:

Sample Size ↑
     ↓
Standard Error ↓
     ↓
Confidence Interval becomes narrower

Therefore, larger samples generally provide more precise estimates.

6. Margin of Error

The margin of error represents the amount added and subtracted from the estimate.

Margin of Error
= Critical Value × Standard Error

Therefore:

Confidence Interval
= Estimate ± Margin of Error

Example:

Mean = 50
Margin of Error = 3

95% CI = 50 ± 3

Lower Limit = 47
Upper Limit = 53

Therefore:

95% CI = (47, 53)
7. Z-Based Confidence Interval

When the population standard deviation is known, a confidence interval for the population mean can be calculated using:

CI = x̄ ± z* × (σ / √n)

where:

x̄ = sample mean
σ = population standard deviation
n = sample size
z* = critical z-value

Common z-values are:

Confidence Level	z*
90%	1.645
95%	1.960
99%	2.576

For a 95% confidence interval:

CI = x̄ ± 1.96 × SE
8. t-Based Confidence Interval

When the population standard deviation is unknown, the t-distribution is generally used.

CI = x̄ ± t* × (s / √n)

where:

x̄ = sample mean
s = sample standard deviation
n = sample size
t* = critical t-value

Degrees of freedom:

df = n - 1

The t-distribution has heavier tails than the standard normal distribution, particularly for smaller samples.

9. Example

Suppose:

Sample Mean = 100
Sample SD = 10
Sample Size = 25

First calculate the standard error:

SE = 10 / √25
   = 10 / 5
   = 2

For a 95% confidence interval with:

df = 25 - 1
   = 24

Suppose the appropriate t critical value is approximately:

t* = 2.064

Margin of error:

ME = 2.064 × 2
   = 4.128

Therefore:

95% CI = 100 ± 4.128
Lower Limit = 95.872
Upper Limit = 104.128

Therefore:

95% CI ≈ (95.87, 104.13)
10. Factors Affecting Confidence Interval Width
Confidence Level

Higher confidence levels produce wider intervals.

90% → narrower
95% → wider
99% → widest
Variability

Higher standard deviation increases uncertainty and generally produces a wider interval.

Sample Size

Larger sample sizes reduce standard error and generally produce narrower intervals.

Sample Size ↑
     ↓
Standard Error ↓
     ↓
Confidence Interval ↓
11. Confidence Interval for a Proportion

Confidence intervals can also be used to estimate population proportions.

For example:

80 out of 100 patients respond to a treatment.

The sample proportion is:

p̂ = 80 / 100
   = 0.80

A confidence interval can then be calculated to estimate the population response proportion.

Applications include:

Disease prevalence
Treatment response
Mutation frequency
Diagnostic test results
Survival proportions
12. Confidence Intervals in Biological Research

Confidence intervals are useful when reporting experimental results.

For example:

Mean Gene Expression = 12.4

95% CI = 11.8 – 13.0

Instead of reporting only the estimated mean:

12.4

the confidence interval also communicates the uncertainty and precision associated with the estimate.

Confidence intervals can be used for:

Gene-expression measurements
Clinical measurements
Treatment effects
Disease prevalence
Biomarker studies
Experimental measurements
Population estimates
13. Confidence Interval vs Standard Deviation

Confidence intervals and standard deviation provide different information.

Standard Deviation

Standard deviation describes variability among individual observations.

SD → Variability in the Data
Confidence Interval

A confidence interval describes uncertainty around an estimated population parameter.

CI → Uncertainty in the Estimate

For example:

Mean = 50
SD = 8
95% CI = 47 – 53

The SD and CI should therefore not be treated as interchangeable quantities.

14. Confidence Interval vs Prediction Interval

A confidence interval is used to estimate a population parameter.

A prediction interval is used to estimate where a future individual observation may fall.

Confidence Interval
→ Population Parameter

Prediction Interval
→ Future Observation

Prediction intervals are generally wider because they account for both uncertainty in the estimated parameter and individual variation.

15. Interpretation

Suppose a study reports:

Mean = 25.4
95% CI = 23.1 – 27.7

The result can be interpreted as an estimate of the population mean with a 95% confidence interval from 23.1 to 27.7.

Avoid interpreting it as:

"There is a 95% probability that the true mean is between
23.1 and 27.7."

The population parameter is treated as fixed, while the confidence interval is what would vary across repeated samples.

16. Confidence Interval Workflow
Collect Biological Data
        ↓
Calculate Sample Statistic
        ↓
Calculate Standard Error
        ↓
Select Confidence Level
        ↓
Determine Critical Value
        ↓
Calculate Margin of Error
        ↓
Calculate Confidence Interval
        ↓
Interpret the Result
17. Quick Revision
Confidence Interval
= Estimate ± Margin of Error

Margin of Error
= Critical Value × Standard Error

For a mean:

SE = s / √n

t-based CI:

CI = x̄ ± t* × (s / √n)

Degrees of freedom:

df = n - 1

Remember:

Sample Size ↑
→ Standard Error ↓
→ Confidence Interval becomes narrower

Variability ↑
→ Confidence Interval becomes wider

Confidence Level ↑
→ Confidence Interval becomes wider
18. Key Takeaways
A confidence interval provides a range of plausible values for a population parameter based on sample data.
The general structure is Estimate ± Margin of Error.
Larger samples generally produce narrower confidence intervals.
Greater variability produces wider confidence intervals.
Higher confidence levels produce wider intervals.
The z-distribution or t-distribution may be used depending on the statistical setting.
Confidence intervals communicate both an estimate and its uncertainty.
They are widely useful in biological, biomedical, and clinical data analysis.
Conclusion

Confidence intervals provide a practical way to communicate the uncertainty and precision of statistical estimates.

In biological research, experimental conclusions are usually based on samples rather than entire populations. Confidence intervals therefore help present statistical estimates together with information about their uncertainty.
