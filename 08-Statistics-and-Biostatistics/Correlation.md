Correlation

Correlation is a statistical method used to measure the strength and direction of the relationship between two variables.

1. Basic Idea

Suppose we want to investigate whether two biological variables are related.

Examples:

Gene expression vs disease severity
Age vs blood pressure
Drug concentration vs response
Body weight vs biomarker level

Correlation helps answer:

Do the two variables tend to change together?

It does not by itself establish that one variable causes the other.

Drag points
2
4
6
8
10
2
4
6
8
X
Y
Linear correlation is positive (r = 0.98).
Negative
Near zero
Positive
Negative
Near zero
Positive
Give feedback

2. Types of Correlation
Positive Correlation

Both variables tend to increase together.

X ↑ → Y ↑

Example:

Gene expression ↑
        ↓
Biomarker level tends to ↑
Negative Correlation

One variable tends to increase while the other decreases.

X ↑ → Y ↓

Example:

Drug concentration ↑
        ↓
Disease-associated marker tends to ↓
No Correlation

There is no clear linear relationship between the variables.

X changes
   ↓
Y shows no consistent linear pattern
3. Pearson Correlation Coefficient

The most commonly used measure of linear correlation is the Pearson correlation coefficient, represented by:

r

Its value ranges from:

-1 ≤ r ≤ +1
Interpretation
r value	General interpretation
+1	Perfect positive linear relationship
0	No linear correlation
-1	Perfect negative linear relationship

Values between these extremes indicate different strengths of linear association.

For example:

r = +0.85 → strong positive linear association
r = -0.80 → strong negative linear association
r = +0.10 → weak positive linear association
r = -0.05 → very weak negative linear association

The exact description of "weak", "moderate", or "strong" depends on the scientific context.

4. Pearson Correlation Formula

The Pearson correlation coefficient can be calculated as:

r =
Σ[(x - x̄)(y - ȳ)]
--------------------------------
√[Σ(x - x̄)² × Σ(y - ȳ)²]

where:

x = individual value of variable X
y = individual value of variable Y
x̄ = mean of X
ȳ = mean of Y
5. Understanding the Sign of r

The sign tells us the direction of the linear relationship.

r > 0
→ Positive relationship

r < 0
→ Negative relationship

r ≈ 0
→ Little or no linear relationship

For example:

r = +0.72

means that higher values of one variable tend to be associated with higher values of the other.

r = -0.72

means that higher values of one variable tend to be associated with lower values of the other.

6. Understanding the Magnitude

The magnitude of r indicates how closely the data follow a linear pattern.

Values closer to:

+1 → stronger positive linear association

-1 → stronger negative linear association

 0 → weaker linear association

For example:

r = 0.95

indicates a very strong positive linear association.

r = -0.90

indicates a very strong negative linear association.

r = 0.02

indicates almost no linear association.

7. Scatter Plot

A scatter plot is commonly used to visualize correlation.

Y
│             •
│          •
│       •
│    •
│ •
└──────────────── X

The points generally move upward from left to right, indicating positive correlation.

Negative correlation:

Y
│ •
│    •
│       •
│          •
│             •
└──────────────── X

No clear linear correlation:

Y
│    •       •
│       •
│ •          •
│      •
│           •
└──────────────── X
8. Correlation Does Not Mean Causation

This is one of the most important concepts.

If two variables are correlated:

X ↔ Y

it does not automatically mean:

X causes Y

There may be:

A third variable
Confounding factors
Indirect relationships
Coincidental association
Reverse causation

Therefore:

Correlation describes association, not necessarily causation.

9. Example in Biology

Suppose researchers measure:

Gene A expression
        vs
Disease severity

They obtain:

r = 0.78

This indicates a positive linear association between the two measured variables.

It does not by itself prove that increased expression of Gene A causes greater disease severity.

Additional experimental evidence would be required to investigate causality.

10. Correlation and Gene-Expression Analysis

Correlation is particularly useful in computational biology.

For example:

Gene A expression
        ↓
Correlation analysis
        ↓
Gene B expression

A high positive correlation could indicate that two genes have similar expression patterns across samples.

Researchers may investigate whether correlated genes are involved in:

The same biological pathway
Similar cellular processes
Common regulatory mechanisms
Related disease mechanisms

However, correlation alone does not establish a shared biological mechanism.

11. Pearson vs Spearman Correlation

Two commonly used correlation measures are:

Pearson Correlation

Measures linear association between variables.

Pearson → Linear relationship
Spearman Correlation

Measures the association between the ranks of variables and is useful for monotonic relationships that may not be linear.

Spearman → Rank-based monotonic relationship
Feature	Pearson	Spearman
Based on	Original values	Ranks
Main relationship	Linear	Monotonic
Sensitive to outliers	More sensitive	Generally less sensitive
Can be useful for non-normal/ordinal data	More limited	Often useful

The appropriate method depends on the data and research question.

12. Correlation and Outliers

An outlier is an observation that is unusually far from the other observations.

Outliers can substantially influence Pearson correlation.

Example:

Most observations:
Strong positive pattern

One extreme observation:
        ↓
Correlation may change considerably

Therefore, scatter plots should be examined before interpreting a correlation coefficient.

13. Correlation and Sample Size

The reliability of a correlation estimate is affected by sample size.

A small dataset can produce an unstable correlation estimate.

Small sample
    ↓
Greater uncertainty

Larger sample
    ↓
More information about the relationship

Statistical significance and effect size should be considered separately.

14. Correlation vs Covariance

Both covariance and correlation describe how two variables vary together.

Covariance

Indicates the direction of joint variation but depends on the units of the variables.

Correlation

Standardizes covariance and produces a unitless value between -1 and +1.

Therefore:

Covariance
→ Depends on measurement units

Correlation
→ Unitless
→ -1 to +1
15. Biological Applications

Correlation analysis can be used for:

Gene-expression relationships
Biomarker analysis
Clinical measurements
Phenotype relationships
Protein-expression studies
Environmental and biological measurements
Multi-omics data exploration

For example:

Gene expression
       ↕
Protein abundance

or:

Gene expression
       ↕
Disease severity
16. Basic Python Example
import numpy as np

# Example biological measurements
gene_expression = np.array([2.1, 3.2, 4.0, 5.1, 6.3])
disease_score = np.array([10, 15, 19, 25, 30])

# Pearson correlation
correlation = np.corrcoef(gene_expression, disease_score)[0, 1]

print("Pearson correlation coefficient:", correlation)

The resulting value gives the Pearson correlation coefficient between the two variables.

17. Correlation Analysis Workflow
Collect paired observations
        ↓
Check the data
        ↓
Visualize using scatter plot
        ↓
Select appropriate correlation method
        ↓
Calculate correlation coefficient
        ↓
Assess statistical significance when appropriate
        ↓
Interpret direction and strength
        ↓
Consider biological context
18. Quick Revision
Correlation
→ Measures association between two variables

Pearson correlation
→ Measures linear association

Range:
-1 ≤ r ≤ +1

r > 0
→ Positive association

r < 0
→ Negative association

r ≈ 0
→ Little or no linear association

Important:
Correlation ≠ Causation
19. Key Takeaways
Correlation measures the association between two variables.
Pearson's r measures linear association.
The correlation coefficient ranges from -1 to +1.
Positive values indicate a positive linear association.
Negative values indicate a negative linear association.
Values closer to ±1 indicate stronger linear association.
Scatter plots are useful for visually examining relationships.
Outliers can strongly affect correlation.
Pearson and Spearman correlation answer somewhat different questions.
Correlation does not establish causation.
Correlation analysis has many applications in biological and biomedical research.
Conclusion

Correlation is an important statistical tool for exploring relationships between biological variables. In bioinformatics and biological data analysis, it can help identify patterns between gene expression, biomarkers, clinical measurements, and other variables. However, correlation should be interpreted alongside visualization, statistical uncertainty, experimental design, and biological context.
