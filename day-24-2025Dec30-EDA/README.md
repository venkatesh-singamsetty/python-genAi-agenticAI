# Exploratory Data Analysis (EDA) -- Foundation of Machine Learning

## 1. What is EDA?

Exploratory Data Analysis (EDA) is the process of understanding,
cleaning, transforming, and preparing raw data so it can be effectively
used by Machine Learning (ML) models.

**Key Point:**\
EDA is the foundation of Machine Learning. Without proper EDA, ML models
fail to produce reliable results.

------------------------------------------------------------------------

## 2. Why EDA is Important for Machine Learning

-   ML models cannot work on raw or dirty data
-   Data quality directly impacts model accuracy
-   EDA helps identify:
    -   Patterns
    -   Relationships
    -   Missing values
    -   Outliers
    -   Irrelevant variables

**Rule:**\
Bad data → Bad model\
Clean data → Accurate model

------------------------------------------------------------------------

## 3. EDA Workflow -- 7 Key Steps

### 0. Business Understanding

Understand the business problem before working with data.

**Domains:** 
- Banking 
- Services 
- Manufacturing 
- Supply Chain (SCM) 
- FMCG 
- Product-based companies

No business runs without customers. Most real-world roles are
non-technical, so ML must solve business problems.

------------------------------------------------------------------------

### 1. Variable Identification

Variable = Column = Attribute

**Types of Variables:**
- Independent Variable (IV / X): Input feature 
- Dependent Variable (DV / Y): Target variable

**Example (Family Analogy):**
- Dad (Govt Employee) → Dependent Variable (Y) 
- Mom (Housewife) → Independent Variable (X1) 
- Son (4th Class) → Independent Variable (X2) 
- Daughter (3rd Class) → Independent Variable (X3)

**ML Formula:** y = m1x1 + m2x2 + m3x3

------------------------------------------------------------------------

### 2. Univariate Analysis

Analysis of a single variable. 
- Distribution 
- Mean, Median, Mode 
- Skewness

------------------------------------------------------------------------

### 3. Bivariate Analysis

Relationship between two variables. 
- IV vs DV 
- IV vs IV

Examples: 
- Experience vs Salary 
- Area vs House Price

------------------------------------------------------------------------

### 4. Outlier Treatment

Outliers are extreme values that affect model learning.

Techniques: 
- IQR 
- Z-score 
- Capping 
- Removal (business-driven)

------------------------------------------------------------------------

### 5. Missing Value Treatment

Missing values can cause bias and model failure.

Examples: 
- Missing age 
- Missing salary

------------------------------------------------------------------------

### 6. Variable Imputation

Replacing missing values with: 
- Mean / Median 
- Mode 
- Forward / Backward fill 
- Model-based imputation

------------------------------------------------------------------------

### 7. Variable Creation (Feature Engineering)

Creating new meaningful variables.

Examples: 
- Date → Year, Month, Day 
- Salary → Salary range 
- Total Spend → Monthly average spend

------------------------------------------------------------------------

## 4. Machine Learning Types

### Supervised Learning

-   Structured data
-   Labeled data
-   Stored in SQL databases (MySQL, PostgreSQL, Oracle)

#### Regression

Dependent Variable is continuous.

Examples: 
- House price 
- Stock price 
- Gold price 
- Flight ticket price

Algorithms: 
- Linear Regression 
- Multiple Linear Regression 
- Polynomial Regression 
- Lasso, Ridge 
- SVR 
- KNN Regression 
- Time Series

------------------------------------------------------------------------

#### Classification

Dependent Variable is binary or categorical.

Examples: 
- Fraud / Non-Fraud 
- Spam / Non-Spam 
- Pass / Fail

Algorithms: 
- Logistic Regression 
- SVM 
- KNN 
- Naive Bayes 
- Decision Tree 
- Random Forest

------------------------------------------------------------------------

### Unsupervised Learning

-   Unstructured data
-   Unlabeled data
-   Stored in NoSQL databases (MongoDB, Cassandra, HBase)

#### Clustering

-   No dependent variable
-   Grouping similar data

Algorithms: 
- K-Means 
- PCA

------------------------------------------------------------------------

## 5. Vector Databases & LLMs

Used in RAG (Retrieval Augmented Generation) models.

Vector Databases: 
- Pinecone 
- FAISS 
- Chroma 
- Milvus 
- Qdrant

Used to store text embeddings for LLM-based applications.

------------------------------------------------------------------------

## 6. Reinforcement Learning

-   Model interacts with environment
-   Uses agents
-   Learns via reward and punishment

Examples: 
- Game AI 
- Robotics 
- Autonomous systems

------------------------------------------------------------------------

## 7. Key Takeaways

-   EDA is mandatory, not optional
-   80% of ML success depends on data quality
-   Algorithms come after EDA
-   Better EDA beats complex models

------------------------------------------------------------------------
