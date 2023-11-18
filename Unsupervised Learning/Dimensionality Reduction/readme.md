# What is Dimensionality Reduction?

Reduce the number of inputs in predictive models by combining original variables that **are correlated with one another** into a smaller number of independent information-rich variables.

## Table of Contents

- [What is Dimensionality Reduction?](#what-is-dimensionality-reduction)
  - [Table of Contents](#table-of-contents)
  - [PCA vs Factor Analysis](#pca-vs-factor-analysis)
    - [Principal Component Analysis (PCA):](#principal-component-analysis-pca)
    - [Factor Analysis (FA):](#factor-analysis-fa)
    - [When to Use PCA or FA:](#when-to-use-pca-or-fa)
  - [Types of Business Questions Answered](#types-of-business-questions-answered)
  - [Types of Data Input](#types-of-data-input)
  - [Useful visuals and metrics](#useful-visuals-and-metrics)
    - [Visuals](#visuals)
    - [Metrics](#metrics)
  - [Small Example](#small-example)
    - [PCA](#pca)
    - [Factor Analysis](#factor-analysis)

## PCA vs Factor Analysis

**Principal Component Analysis (PCA) and Factor Analysis (FA)** are both techniques used for dimensionality reduction in data analysis, but they have different objectives and underlying assumptions. Understanding these differences is crucial for choosing the appropriate method for a given dataset or research question.

### Principal Component Analysis (PCA):

1. **Objective:**

   - PCA aims to reduce the dimensionality of a dataset by transforming the original variables into a new set of uncorrelated variables, called principal components.
   - These components are linear combinations of the original variables and are ordered so that the first few retain most of the variation present in all of the original variables.
2. **Assumptions:**

   - PCA assumes that the total variance in the data is important and seeks to preserve as much of this variance as possible.
   - It doesn't differentiate between shared and unique variance.
3. **Use Cases:**

   - PCA is used when the goal is data reduction or when you want to identify new, meaningful underlying variables.
   - It is ideal for pattern recognition, noise reduction, and feature extraction in machine learning.
4. **Interpretation:**

   - The principal components are not easily interpretable in terms of the original variables.
   - Components are orthogonal (uncorrelated), and each represents a direction in the feature space along which the data varies the most.

### Factor Analysis (FA):

1. **Objective:**

   - Factor Analysis seeks to identify underlying factors that explain the patterns of correlations within a set of observed variables.
   - It assumes that any observed variable can be primarily described using a small number of unobserved latent factors.
2. **Assumptions:**

   - FA works under the assumption that the observed variables have underlying correlations.
   - It distinguishes between shared variance (common factors) and unique variance (specific factors and error).
3. **Use Cases:**

   - FA is mainly used in social sciences, psychology, and other fields where the research is about identifying underlying constructs.
   - It's beneficial when you want to identify latent variables influencing observed behavior.
4. **Interpretation:**

   - The factors are potentially interpretable and might represent underlying processes or constructs.
   - Factors are not necessarily orthogonal.

### When to Use PCA or FA:

- **Use PCA when:**

  - The primary goal is dimensionality reduction or feature extraction.
  - You are dealing with high-dimensional data and want to preserve as much variance as possible.
  - The data does not necessarily have a hypothesized underlying structure.
- **Use FA when:**

  - You aim to understand the underlying structure of data or latent constructs.
  - You are working in fields like psychology or social sciences, where exploring underlying factors is common.
  - There is a theoretical basis to assume that observed variables are influenced by some latent factors.

In summary, PCA is more about preserving variance and transforming variables, while Factor Analysis is about understanding the underlying structure or constructs in the data. The choice between PCA and FA should be guided by the specific goals of your analysis and the nature of your data.

## Types of Business Questions Answered

PCA and Factor Analysis don't necessarily help a business answer questions on their own, they are inputs into to predictive models that do.

## Types of Data Input

Correlated original factors with linear relationships.

## Useful visuals and metrics

### Visuals

Scree plot - A plot of the eigenvalues of the principal components, above 1 is considered significant.

### Metrics

- Bartletts Test of Sphericity - Tests is correlation matrix is an identity matrix, which would indicate that the variables are unrelated and PCA is not suitable. A significant result suggests that there are correlations in the data and PCA is a viable option.
- Kaiser-Meyer-Olkin (KMO) Measure of Sampling Adequacy - Tests proportion of variance among variables that might be common variance. Greater than 0.6 is considered significant.

## Small Example

Also in jupyter notebooks, here for easy reference.

### PCA

```python
df_pca = df_standardized.copy()

pca = PCA(n_components=4)
X2D = pca.fit_transform(df_pca.drop(['Public (1)_Private (2)', 'GraduationRate'], axis=1))

print(pca.explained_variance_ratio_)

cumulative_sum = 0

for value in pca.explained_variance_ratio_:
    cumulative_sum += value
    print(cumulative_sum)


df_standardized.head()


components = pca.components_

component_idx = 0
component_loadings = components[component_idx].argsort()[::-1]
variables_with_highest_loadings = [list(df_pca.columns)[i] for i in component_loadings]
#component_loadings.argsort()

loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3', 'PC4'], index=df_pca.drop(['Public (1)_Private (2)', 'GraduationRate'], axis=1).columns)
loadings
```

### Factor Analysis

```python

```