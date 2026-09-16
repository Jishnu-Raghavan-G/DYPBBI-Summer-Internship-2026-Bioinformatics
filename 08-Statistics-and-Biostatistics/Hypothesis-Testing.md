Introduction

Hypothesis testing is a statistical framework used to evaluate whether the observed data provide sufficient evidence against a specified null hypothesis.

In biological research, hypothesis testing can be used when comparing groups, evaluating experimental effects, or investigating whether an observed difference could reasonably occur under a particular statistical assumption.

Basic Idea

The general workflow is:

Research Question
       ↓
Define Hypotheses
       ↓
Choose Statistical Test
       ↓
Set Significance Level
       ↓
Collect / Analyze Data
       ↓
Calculate Test Statistic
       ↓
Calculate P-value
       ↓
Interpret Statistical Evidence
Null Hypothesis

The null hypothesis (H₀) represents the assumption being tested.

It commonly states that there is:

No difference
No association
No effect
No relationship

For example, when comparing gene expression between two groups:

H₀:
There is no difference in the population-level
gene-expression measure between the two groups.
Alternative Hypothesis

The alternative hypothesis (H₁ or Hₐ) represents the competing hypothesis.

For the same example:

H₁:
There is a difference in the population-level
gene-expression measure between the two groups.

The exact hypotheses depend on the research question.

Significance Level

The significance level, commonly represented by α, is selected before evaluating the statistical result.

A commonly used value is:

α = 0.05

This represents a predefined threshold for interpreting the statistical evidence against the null hypothesis.

The significance level should not be changed simply because a particular result is obtained.

Test Statistic

A statistical test generally calculates a test statistic from the observed data.

The exact formula depends on the test being performed.

Conceptually:

Observed Data
     ↓
Statistical Test
     ↓
Test Statistic
     ↓
P-value

Different tests are appropriate for different types of data and experimental designs.

Common Statistical Tests
One-Sample Test

Used when a sample is compared with a specified reference value.

Example:

Observed sample mean
        ↓
Compare with
        ↓
Specified population/reference value
Two-Sample Test

Used when measurements from two groups are compared.

For example:

Group A
Healthy samples
      ↓
      Compare
      ↑
Group B
Disease samples

The appropriate test depends on the study design and assumptions.

Paired Test

Used when observations are naturally paired.

Examples can include:

Before vs after measurements on the same subjects
Matched biological samples
ANOVA

Analysis of Variance (ANOVA) can be used to compare means across multiple groups under an appropriate study design.

For example:

Group A ─┐
Group B ─┼──→ ANOVA
Group C ─┘

If the overall test indicates evidence of differences, additional analysis may be required to determine which groups differ.

One-Tailed and Two-Tailed Tests
Two-Tailed Test

A two-tailed test considers deviations in either direction.

        Rejection       Rejection
           ↓               ↓
───────────|───────|───────|──────────
         -critical   0   +critical

It is appropriate when the research question concerns whether there is a difference without specifying its direction beforehand.

One-Tailed Test

A one-tailed test considers a specified direction.

───────────────────────────────|──────→
                               Critical

The direction must be justified by the research question and study design.

Type I Error

A Type I error occurs when the null hypothesis is rejected even though it is true.

Conceptually:

H₀ is actually true
       ↓
Reject H₀
       ↓
Type I Error

The significance level α is related to the maximum Type I error probability under the assumptions of the testing procedure.

Type II Error

A Type II error occurs when the null hypothesis is not rejected even though the alternative hypothesis is true.

H₁ is actually true
       ↓
Fail to reject H₀
       ↓
Type II Error

The probability of a Type II error is commonly represented by β.

Statistical power is:

Power = 1 − β
Reject vs Fail to Reject

Statistical hypothesis testing is commonly expressed using:

If p-value ≤ α:
    Reject H₀

If p-value > α:
    Fail to reject H₀

A more careful interpretation is that the result provides sufficient or insufficient statistical evidence against the null hypothesis at the chosen significance level.

It is generally preferable to say "fail to reject the null hypothesis" rather than "accept the null hypothesis."

Example

Suppose gene-expression measurements are compared between two groups.

The analysis gives:

α = 0.05

p-value = 0.02

Since:

0.02 < 0.05

the result meets the predefined statistical significance criterion.

The appropriate statistical conclusion is:

Reject H₀ at α = 0.05.

This does not by itself establish that the observed difference is biologically important.

Statistical vs Biological Significance

These concepts should be distinguished.

Statistical Significance

Addresses whether the observed data provide sufficient evidence against the null hypothesis according to the specified statistical procedure.

Biological Significance

Addresses whether the magnitude and nature of the observed difference are meaningful in the biological context.

For example:

Very small effect
      +
Very large sample
      ↓
Could produce statistical significance

Therefore, statistical significance should not automatically be equated with biological importance.

Assumptions

Statistical tests often rely on assumptions.

Depending on the test, these may include:

Independence
Appropriate measurement scale
Distributional assumptions
Homogeneity of variance
Appropriate sampling/design

The assumptions should be considered before interpreting the result.

Multiple Testing

Bioinformatics datasets can involve testing thousands of hypotheses simultaneously.

For example:

Gene 1  → Test
Gene 2  → Test
Gene 3  → Test
...
Gene 10,000 → Test

If many tests are performed, some small p-values can occur by chance.

Therefore, multiple-testing correction is important in large-scale analyses.

In transcriptomics, adjusted p-values are commonly used during differential-expression analysis to control for the effects of performing many statistical tests. The DYPBBI asthma case study similarly used statistical filtering before downstream functional and network analysis.

Hypothesis Testing in Bioinformatics

A simplified bioinformatics example is:

Gene-Expression Dataset
        ↓
Define Comparison
        ↓
Statistical Analysis
        ↓
P-values
        ↓
Multiple-Testing Correction
        ↓
Adjusted P-values
        ↓
Identify Statistically Supported Genes

In the asthma transcriptomics workflow, healthy and asthma groups were compared using GEO2R, followed by differential-expression analysis and statistical filtering before downstream analyses.

Common Mistakes
Mistake 1: Treating p-value as the probability that H₀ is true

A p-value does not directly give the probability that the null hypothesis is true.

Mistake 2: Saying "p = 0.03 means there is a 3% chance the result happened by chance"

That is an oversimplification and is not the correct definition of a p-value.

Mistake 3: Ignoring the study design

The statistical test must match the experimental design and data.

Mistake 4: Ignoring Multiple Testing

Testing many genes without appropriate correction can produce misleading numbers of apparently significant results.

Mistake 5: Equating statistical significance with biological importance

A statistically significant result may have little biological relevance, depending on its effect size and context.

Quick Revision
Hypothesis Testing

H₀ → Null Hypothesis
H₁ → Alternative Hypothesis
α  → Significance Level
β  → Type II Error Probability
Power = 1 − β
p-value → Evidence against H₀
Decision Framework
             p-value
                ↓
       ┌────────┴────────┐
       ↓                 ↓
    p ≤ α              p > α
       ↓                 ↓
 Reject H₀         Fail to reject H₀
Conclusion

Hypothesis testing provides a structured method for evaluating statistical evidence. It involves defining hypotheses, selecting an appropriate test, specifying a significance level, calculating a test statistic and p-value, and interpreting the result in the context of the research question.

For bioinformatics, hypothesis testing becomes especially important when analyzing biological datasets containing many measurements, such as gene-expression data, where statistical significance, multiple testing, effect size, and biological relevance must be considered together.
