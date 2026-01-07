
# Exploratory Data Analysis (EDA) – Machine Learning Foundations

## Overview
Exploratory Data Analysis (EDA) is the foundation of any Machine Learning (ML) project.  
It helps convert **raw data into clean, structured, and meaningful data** that ML models can learn from.

This document explains **core EDA concepts** with simple definitions and real-world relevance.

---

## 1. Variable Identification
A **variable** is a column in an Excel sheet or dataset.  
Also known as **feature** or **attribute**.

### Types of Variables
- **Dependent Variable (DV / Target / y)**
  - Output variable
  - What the model predicts
  - Example: Price, Churn, Sales

- **Independent Variables (IV / Features / x1, x2, x3...)**
  - Input variables used to predict DV
  - Example: Age, Salary, Experience

---

## 2. Univariate Analysis
Analysis of **one variable at a time**.

### Purpose
- Understand data distribution
- Identify missing values
- Detect outliers

### Techniques
- Numerical: Mean, Median, Mode, Histogram, Boxplot
- Categorical: Value counts, Bar charts

---

## 3. Bivariate Analysis
Analysis of **two variables together**.

### Correlation
Correlation measures the **relationship between two numerical variables**.

#### Correlation Range
- Range: **-1 to +1**
  - **+1** → Strong positive correlation
  - **0** → No correlation
  - **-1** → Strong negative correlation

#### Types
- Positive Correlation (0 to +1)
- Negative Correlation (-1 to 0)
- No Correlation (0)

---

## 4. Outlier Treatment
An **outlier** is an extreme or abnormal data point.

### Detection Methods
- Boxplot
- Histogram
- Scatter Plot

### Impact on ML Models
- Distorts mean
- Reduces accuracy
- Misleads algorithms (Linear Regression, KNN)

### Real-Time Handling
- Outliers usually **cannot be removed**
- Their impact is **adjusted**

### Solution
- Use **probability functions**
- Common function: **Sigmoid Curve**
  - Converts values between 0 and 1
  - Reduces extreme impact

---

## 5. Missing Value Treatment

### Types of Data
- **Numerical** → Numbers
- **Categorical** → Text / Labels

### Handling Strategies

#### Numerical Variables
- Mean (normal distribution)
- Median (outliers present)
- Mode (less common)

#### Categorical Variables
- Mode
- KNN Imputation

---

## 6. Variable Creation
Creating **new features** from existing data.

### Examples
- Annual Salary from Monthly Salary
- Experience Level from Years of Experience

---

## 7. Variable Transformation (Imputation & Encoding)

ML models only understand **numerical data**.

### Encoding Techniques

#### One-Hot Encoding (Dummy Variables)
- Converts categories into binary columns
- Number of classes = number of new columns

#### Label Encoding
- Converts categories into numeric values (0,1,2...)
- Used when data has **order**
- Suitable for tree-based models

---

## Key Takeaways
- EDA prepares data for ML
- Clean data improves accuracy
- Proper encoding is mandatory
- Outliers and missing values must be handled carefully
