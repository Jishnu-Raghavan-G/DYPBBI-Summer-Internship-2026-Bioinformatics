Introduction

Probability is the mathematical framework used to describe uncertainty and the likelihood of events.

In biological research, uncertainty is present in measurements, experiments, sampling, and statistical inference. Probability provides the foundation for many statistical methods used to analyze biological data.

Basic Terms
Experiment

An experiment is a process that produces an observable outcome.

Examples:

Measuring gene expression
Counting cells
Testing whether a sample contains a particular molecule
Measuring enzyme activity
Outcome

An outcome is one possible result of an experiment.

For example, when a coin is tossed:

Possible outcomes = Head, Tail
Sample Space

The sample space is the set of all possible outcomes.

For a coin:

S = {Head, Tail}

For a six-sided die:

S = {1, 2, 3, 4, 5, 6}
Event

An event is a collection of one or more outcomes from the sample space.

For a die:

Event A = obtaining an even number

A = {2, 4, 6}
Probability of an Event

For equally likely outcomes:

P(A) = Number of favorable outcomes
       ───────────────────────────────
       Total number of possible outcomes

For example, the probability of obtaining an even number when rolling a fair die is:

P(Even) = 3 / 6
        = 1 / 2
        = 0.5

Therefore, the probability is 0.5 or 50%.

Range of Probability

Probability always lies between 0 and 1.

0 ≤ P(A) ≤ 1

Where:

P(A) = 0 → Impossible event

P(A) = 1 → Certain event
Complementary Events

The complement of event A represents the event that A does not occur.

It is written as:

P(Aᶜ) = 1 − P(A)

For example, if:

P(A) = 0.7

then:

P(Aᶜ) = 1 − 0.7
       = 0.3
Addition Rule

The probability that either event A or event B occurs is:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

The subtraction term prevents the shared outcomes from being counted twice.

If two events cannot occur simultaneously, they are mutually exclusive.

For mutually exclusive events:

P(A ∩ B) = 0

Therefore:

P(A ∪ B) = P(A) + P(B)
Multiplication Rule

The probability that both events occur can be expressed as:

P(A ∩ B) = P(A) × P(B | A)

where P(B | A) is the probability of B occurring given that A has occurred.

Independent Events

Two events are independent when the occurrence of one does not change the probability of the other.

For independent events:

P(A ∩ B) = P(A) × P(B)

For example, if two fair coin tosses are independent:

P(Head on first toss) = 1/2

P(Head on second toss) = 1/2

Therefore:

P(Head and Head)
= 1/2 × 1/2
= 1/4
Conditional Probability

Conditional probability describes the probability of one event given that another event has already occurred.

It is written as:

P(A | B) = P(A ∩ B)
           ─────────
              P(B)

provided that P(B) > 0.

In biological research, conditional probability can be useful when considering probabilities under a particular experimental or biological condition.

Random Variables

A random variable assigns numerical values to outcomes of a random process.

There are two major types.

Discrete Random Variable

A discrete random variable takes distinct, countable values.

Examples:

Number of cells
Number of mutations
Number of colonies
Number of patients responding to a treatment
Continuous Random Variable

A continuous random variable can take values over a continuous range.

Examples:

Protein concentration
Cell size
Blood pressure
Temperature
Gene-expression measurements
Probability Distributions

A probability distribution describes the probabilities associated with possible values of a random variable.

Common distributions include:

Binomial distribution
Normal distribution
Poisson distribution

Different distributions are appropriate for different types of data and experimental situations.

Binomial Distribution

The binomial distribution describes the number of successes in a fixed number of independent trials when each trial has two possible outcomes.

The probability of obtaining exactly x successes in n trials is:

P(X = x) = C(n,x) pˣ (1 − p)ⁿ⁻ˣ

where:

n = number of trials
x = number of successes
p = probability of success
1 − p = probability of failure

For example, if a fair coin is tossed 5 times, the probability of exactly 3 heads can be calculated using the binomial distribution.

Normal Distribution

The normal distribution is a continuous probability distribution with a symmetric, bell-shaped form.

                 │
              █████
            █████████
          █████████████
        █████████████████
     ───────────────────────
              Mean

For a normal distribution:

Mean = Median = Mode

The normal distribution is widely used in statistical modelling and inference.

Expected Value

The expected value represents the long-run average value of a random variable.

For a discrete random variable:

E(X) = Σ xP(x)

where x represents possible values and P(x) represents their probabilities.

Probability in Biological Research

Probability is important in several areas of bioinformatics and biology.

Examples include:

Genetic inheritance
Disease risk estimation
Experimental outcomes
Sampling
Statistical hypothesis testing
Probability distributions of biological measurements
Classification and prediction

For example:

Biological Experiment
       ↓
Observed Data
       ↓
Probability Model
       ↓
Statistical Inference
       ↓
Biological Interpretation
Probability and Statistical Testing

Probability forms the foundation of statistical inference.

A simplified relationship is:

Probability
    ↓
Probability Distributions
    ↓
Statistical Tests
    ↓
P-values / Confidence Intervals
    ↓
Inference

Understanding probability therefore helps in understanding later topics such as hypothesis testing and p-values.

Quick Revision
Concept	Meaning
Probability	Measure of likelihood
Sample space	All possible outcomes
Event	One or more outcomes
Complement	Event not occurring
Independent events	One event does not affect another
Conditional probability	Probability given another event
Random variable	Numerical representation of outcomes
Discrete variable	Countable values
Continuous variable	Values over a continuous range
Binomial distribution	Number of successes in fixed trials
Normal distribution	Symmetric continuous distribution
Key Formulas
P(Aᶜ) = 1 − P(A)

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

P(A ∩ B) = P(A)P(B | A)

For independent events:
P(A ∩ B) = P(A)P(B)

P(A | B) = P(A ∩ B) / P(B)

Binomial:
P(X = x) = C(n,x)pˣ(1 − p)ⁿ⁻ˣ
Conclusion

Probability provides the mathematical foundation for describing uncertainty and random variation. Concepts such as events, conditional probability, independence, random variables, and probability distributions are essential for understanding statistical analysis.

In bioinformatics and biological research, probability connects experimental observations with statistical inference and helps provide a quantitative framework for interpreting uncertain biological data.
