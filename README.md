# UnderstandingDepression-DSA210Project

## Project Overview

This project aims to explore the underlying socio-economic and behavioral factors that contribute to depression. By leveraging two university-level student survey datasets, we investigate how academic performance, financial aid, sleep habits, and personal background correlate with depression severity.

Rather than comparing different populations, we adopt complementary datasets from distinct contexts to validate findings across samples and improve confidence in the conclusions. This approach allows us to build a more comprehensive and generalizable understanding of depression risk factors among students.

---

## Objectives

1. **Identify Depression Risk Factors**  
   Examine how academic achievement, sleep duration, financial support, and mental health history relate to depression outcomes.

2. **Enhance Insights Through Multiple Perspectives**  
   Use two complementary student datasets to validate findings from different demographic and academic backgrounds.

3. **Analyze the Role of Academic, Behavioral, and Social Variables**  
   Determine which behavioral and contextual factors most significantly affect mental health, with emphasis on sleep and familial predisposition.

4. **Provide Public Health Insights**  
   Translate results into actionable insights for student well-being programs, especially around sleep habits and support systems.

---

## Motivation

This project blends two key areas of interest: mental health research and data science. Here’s why it matters:

- **A Data-Driven Approach to Mental Health**  
  Understanding depression through statistical testing strengthens the validity of our insights and avoids overreliance on subjective interpretation.

- **Real-World Relevance**  
  Student mental health is increasingly recognized as a public health concern. By identifying key risk factors, this project contributes to targeted intervention strategies.

- **Bridging Complementary Datasets**  
  By analyzing two datasets—one focused on detailed academic and demographic indicators, the other on broader behavioral and stress factors—we create a richer foundation for conclusions.

---

## Dataset

This project uses two survey-based datasets that capture a range of academic, behavioral, and psychological metrics relevant to student well-being.

### **1. uni_depression.csv**
- **Description:** A dataset collected from university students, combining PHQ‑9 depression scores with academic metrics and financial aid indicators.
- **Key Features:**
  - Binned CGPA ranges (e.g., “2.5–3.0”)
  - Scholarship/waiver status
  - PHQ-9 total depression scores

### **2. second_Student_Depression_Dataset.csv**
- **Description:** A broader dataset covering numeric CGPA values, categorized sleep duration, and stress-related variables among students.
- **Key Features:**
  - Depression score (PHQ‑9-style)
  - Sleep duration categories
  - Numeric CGPA values
  - Indicators of financial and academic pressure

---

## Hypotheses

1. **Sleep Duration and Depression**  
   - **H₀:** Sleep duration has no association with depression scores.  
   - **Hₐ:** Shorter sleep durations are associated with higher depression scores.  
   *(Tested via Spearman correlation and one-way ANOVA)*

2. **Family History and Depression**  
   - **H₀:** Family history of mental illness is independent of depression status.  
   - **Hₐ:** Students with a family history are more likely to be depressed.  
   *(Tested via chi-square test)*

3. **CGPA and Depression**  
   - **H₀:** CGPA is not significantly associated with depression.  
   - **Hₐ:** Academic performance differs between depressed and non-depressed students.  
   *(Tested via t-test and Pearson correlation)*

4. **Scholarship Status and Depression**  
   - **H₀:** Scholarship status does not influence depression scores.  
   - **Hₐ:** Scholarship recipients exhibit different depression scores than non-recipients.  
   *(Tested via two-sample t-test)*

---

## Tools and Technologies

This project utilizes the following tools for analysis and visualization:

- **Python**: For data processing and statistical analysis
- **Pandas**: For dataset manipulation and cleaning
- **Matplotlib & Seaborn**: For creating visualizations (histograms, scatterplots, violin plots, etc.)
- **SciPy & Statsmodels**: For performing hypothesis tests and statistical inference

---

## Analysis Plan

1. **Data Processing and Preparation**  
   - Clean and normalize datasets
   - Convert categorical values and handle missing entries

2. **Exploratory Data Analysis (EDA)**  
   - Use visualizations (violin plots, KDEs, heatmaps) to examine how depression varies by sleep, CGPA, and scholarship status

3. **Hypothesis Testing**  
   - Use t-tests, ANOVA, chi-square, and correlation to test for statistical significance of observed patterns

4. **Findings and Insights**  
   - Summarize which variables—sleep, CGPA, financial aid, family history—most strongly relate to student depression

---

## Conclusion

This project uses hypothesis testing to uncover the most statistically supported predictors of depression among students. Sleep duration and family mental health history showed the strongest associations, while CGPA and scholarship status had weaker or non-significant effects. By combining multiple analytical methods and datasets, we gained a clearer view of student mental health and its contributing factors.

---

## AI Assistance Disclosure
ChatGPT was used to revise earlier drafts and improve clarity in this updated README.
