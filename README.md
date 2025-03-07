# MoodTracking-DSA210Project

## Project Overview

For this project, I will be collecting data from **March 8 to May 23**, spanning a total of **77 days**. During this period, I will analyze how various daily factors influence my mood and overall emotional state. By tracking my self-reported mood scores at different times of the day alongside variables such as sleep quality, time spent with friends, personal time, weather conditions, and the points difference between Galatasaray and Fenerbahçe (as a passionate supporter of Galatasaray, I believe it may have an impact on my mood), I aim to uncover patterns that shape my emotional well-being.

Using data visualization and statistical tools, I will explore these relationships and develop hypotheses to test the extent to which external and internal factors influence my daily mood fluctuations. Ultimately, this project will provide insights into the key contributors to emotional well-being and how small adjustments might enhance daily experiences.

---

## Objectives

1. **Identify Mood Influences**  
   Explore the relationship between mood fluctuations and factors such as sleep, social interactions, personal time, weather, and external events.

2. **Understand Key Contributors**  
   Determine which variables have the strongest impact and assess their significance through statistical analysis.

3. **Data-Driven Self-Improvement**  
   Use the insights from the analysis to adjust daily habits and potentially improve emotional well-being.

4. **Apply Data Science Skills**  
   Leverage data analysis and visualization techniques from my DSA 210 course to conduct a meaningful real-world study.

---

## Motivation

This project merges two essential aspects of life: mental well-being and data science. Here’s why it matters:

- **Self-Reflection and Growth**  
  Understanding my emotional patterns will help me make informed decisions about daily habits and improve my overall well-being.
  
- **Scientific Approach to Mood**  
  Rather than relying on subjective feelings, I want to analyze mood trends with data-driven methods.
  
- **Practical Application of Data Science**  
  This is an opportunity to apply theoretical knowledge to a personal and impactful real-world scenario.
  
- **Long-Term Impact**  
  The findings of this study may help establish a framework for tracking and improving emotional well-being over time.

---

## Dataset

The dataset for this project consists of self-reported mood scores and various contextual variables collected over the 77-day period. Here’s what I will be tracking:

### **Mood Tracking (Self-Reported, 1-10 Scale)**
#### **Morning (Upon Waking Up)**
- How do I feel right now?
- How responsible do I feel today?
- How anxious am I?
- Estimated overall rating for the day

#### **Midday (Two Check-ins, Tentatively 2 Hours After Eating)**
- How do I feel right now?
- Optional: Current rating of the day (might be removed based on analysis)

#### **Evening (Before Sleeping)**
- How do I feel right now?
- Final rating of the day
- How much anxiety did I experience today?
- How anxious am I about the future?
- To what extent did I fulfill my responsibilities?
- Would I want to relive this day? (Binary: 0 = No, 1 = Yes)

---

### **External Factors & Contextual Data**
- **Time Spent with Friends** (1-3 scale: 1 = 0-5 minutes, 2 = 5-60 minutes, 3 = More than 60 minutes)
- **Personal Time** (Minutes spent alone for self-care or relaxation)
- **Weather Conditions** (Data retrieved from an external source, with further consideration for personal preference towards rainy/cloudy weather)
- **Galatasaray vs. Fenerbahçe Points Difference** (Daily updated points difference, where positive values mean Galatasaray is leading and negative values mean Fenerbahçe is leading)
- **Sleep Score Calculation**
  - Total sleep duration (scaled by 0.8, e.g., 8 hours * 0.8 = 6.4)
  - Ease of falling asleep (+1.6 points)
  - Ease of waking up (+2.0 points)
  - **Total score out of 10**
- **Work and Study Time**
  - **Class Hours** (Total duration of lectures attended)
  - **Personal Study Time** (Self-directed learning and study sessions)
  - **Total Work and Study Time** (Sum of class and study time)

---

## Hypotheses

1. **Effect of Sleep on Daily Parameters**
   - H₀: Sleep duration and quality have no significant effect on anxiety, general responsibility, or overall mood.
   - Hₐ: Sleep duration and quality significantly impact anxiety levels, sense of responsibility, and overall mood throughout the day.

2. **Impact of Work and Study on Mood and Responsibility**
   - H₀: The amount of time spent studying or working has no measurable effect on mood or the perceived fulfillment of responsibilities.
   - Hₐ: Higher work/study time correlates with increased responsibility fulfillment but may negatively impact mood depending on workload.

3. **Effect of Social Interaction on Mood**
   - H₀: Time spent with friends has no measurable impact on mood fluctuations.
   - Hₐ: Increased social interaction is associated with an improvement in overall mood scores.

4. **Correlation Between Midday and Evening Mood**
   - H₀: Midday mood ratings do not predict evening mood scores.
   - Hₐ: There is a significant correlation between how one feels midday and their overall mood by the end of the day.

5. **Effect of Weather on Emotional Well-being**
   - H₀: Weather conditions have no significant effect on daily mood ratings.
   - Hₐ: Certain weather conditions (e.g., cloudy/rainy days) positively or negatively influence mood depending on personal preference.

6. **Effect of Galatasaray vs. Fenerbahçe Points Difference on Mood**
   - H₀: The points difference between Galatasaray and Fenerbahçe has no effect on mood.
   - Hₐ: A larger positive points difference (Galatasaray leading) improves mood, whereas a decreasing or negative points difference negatively impacts mood.

---

## Tools and Technologies

I will use the following tools for data analysis and visualization:

- **Python**: For data processing and statistical analysis
- **Pandas**: To manage and manipulate data
- **Matplotlib & Seaborn**: For data visualization (line charts, scatter plots, heatmaps)
- **SciPy**: For hypothesis testing and correlation analysis
- **Machine Learning Models**: Advanced prediction and feature importance analysis

---

This project is not just about tracking emotions; it is about leveraging data science to uncover meaningful insights into mental well-being. By understanding the patterns behind emotional fluctuations, I hope to make data-driven improvements in daily life and gain deeper insights into the factors shaping overall well-being.
