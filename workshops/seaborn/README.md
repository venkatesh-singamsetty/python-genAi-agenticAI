## seaborn
- [YouTube: Seaborn workshop](https://www.youtube.com/watch?v=JhfTZ1QWN6A&t=4561s)
- Seaborn is Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics
- https://seaborn.pydata.org/tutorial/color_palettes.html#qualitative-color-palettes

## Run seaborn app
- https://streamlit.io/

```bash
cd /Users/venkat/workspace/gitRepos/python-genAi-agenticAI/workshops/seaborn

python3.12 -m venv .venv
source .venv/bin/activate
python3.12 -m pip install seaborn matplotlib streamlit

streamlit run sns_app.py
```
- Open the app in your browser and navigate to http://localhost:8501/

## Seaborn Plots
1. Scatter Plot → sns.scatterplot()
   - Visualizes relationship between two numeric variables.
   - Optional: hue/size for categorical or continuous encoding.

2. Line Plot → sns.lineplot()
   - Shows trends over ordered numeric or time data.
   - Useful for averages, continuous relationships.

3. Bar Plot → sns.barplot()
   - Compares average (or other estimator) of a numeric variable across categories.
   - Can split by hue for subcategories.

4. Box Plot → sns.boxplot()
   - Summarizes distribution, median, quartiles, and outliers of numeric data across categories.

5. Violin Plot → sns.violinplot()
   - Combines box plot + KDE to show full distribution shape of numeric data across categories.

6. Count Plot → sns.countplot()
   - Shows frequency (counts) of categorical values.
   - Can split by hue for subcategories.

7. Regression Plot → sns.regplot() / sns.lmplot()
   - Shows linear regression trend between numeric variables.
   - Includes confidence interval by default.

8. Histogram → sns.histplot()
   - Shows frequency distribution of a numeric variable.
   - Can overlay KDE for smooth distribution.

9. Pair Plot → sns.pairplot()
    - Creates a matrix of pairwise scatter plots for numeric variables.
    - Diagonal shows distributions; hue can encode categories.

10. Categorical Plot (Catplot) → sns.catplot()
    - Figure-level wrapper for bar, point, strip, box, violin, etc.
    - Good for faceting and multi-category visualization.

11. Joint Plot → sns.jointplot()
    - Plots relationship between two numeric variables + marginal distributions.
    - Supports scatter, regression, KDE, hex plots.

12. Facet Grid → sns.FacetGrid()
    - Creates a grid of subplots based on one or more categorical variables.
    - Can map any plot type to each facet for comparison.

13. Strip Plot → sns.stripplot()
    - Plots all individual observations along a categorical axis.
    - Optional jitter reduces overlap.

14. KDE Plot → sns.kdeplot()
    - Shows smoothed probability density of numeric data.
    - Can compare multiple distributions using hue.

## Tips for EDA:
- Use hue to encode categories for multivariate insight.
- Combine FacetGrid or catplot with different plot types for faceted comparisons.
- Use jitter=True in stripplot to avoid overlapping points.
- Use kde=True in histplot for a smoothed distribution overlay.
- Start with scatterplot, histplot, boxplot, pairplot for initial EDA.
