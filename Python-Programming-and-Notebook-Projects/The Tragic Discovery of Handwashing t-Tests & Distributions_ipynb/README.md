1.	Project Overview
This project analyzes historical hospital records from Vienna General Hospital to uncover the life-saving effect of handwashing in the 19th century.
Through data exploration, statistical analysis, and visualization, it demonstrates how proper hygiene drastically reduced mortality rates, even before germ theory was fully established.
Advanced – The Tragic Discovery of Handwashing: t-Tests & Distributions.

2.	Features
•	Preliminary Data Exploration: Inspect and clean historical mortality datasets.
•	Data Visualization: Plot births and deaths by year and clinic.
•	Statistical Analysis: Compare mortality rates before and after handwashing introduction.
•	t-Test for Significance: Test if the difference in death rates is statistically significant.
•	Distribution Visualization: Plot and interpret data distributions.

3.	Tech Stack
•	Language: Python 3.x
•	Libraries:
o	pandas – Data handling & cleaning
o	matplotlib – Data visualization
o	seaborn – Statistical plotting
o	scipy.stats – t-Tests & statistical methods

4.	How It Works
Preliminary Data Exploration
•	Load historical mortality datasets for Vienna General Hospital.
•	Inspect missing values, data types, and trends.
Yearly Data Split by Clinic
•	Separate data for Clinic 1 and Clinic 2.
•	Plot yearly mortality trends for each clinic.
 Measuring the Effect of Handwashing
•	Identify the point when handwashing was introduced.
•	Compare death rates before and after the change.
Statistical Significance Testing
•	Perform a two-sample t-test on pre- and post-handwashing mortality rates.
•	Interpret the p-value to confirm significance.
Visualizing Distributions
•	Plot histograms and KDE plots for mortality rate distributions.
•	Show how distributions shift after handwashing.

5.	Learning Outcomes
•	Data cleaning & preparation with Pandas.
•	Exploratory Data Analysis (EDA) for real-world historical datasets.
•	Hypothesis testing using t-tests.
•	Statistical data visualization with Matplotlib & Seaborn.