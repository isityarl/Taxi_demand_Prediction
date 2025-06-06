# 🚖 NYC Yellow Taxi Trip Count Forecasting

This project provides a **comprehensive analysis and forecasting** of New York City's Yellow Taxi trip counts using a large dataset spanning from **2011 to 2024**. It leverages **PySpark** for large-scale data processing and implements two advanced machine learning models—**XGBoost** and an **LSTM neural network**—to predict **hourly taxi demand**.

---

## 📌 Overview

The primary goal is to build robust forecasting models that can capture the complex **patterns, trends, and seasonality** in NYC taxi usage over more than a decade.

---
**Results:**
  XGBoost's RMSE: 1974.8699
  LSTM's RMSE: 0.0095

## 📂 Data Source

- **Dataset:** NYC Yellow Taxi Trip Records. Link: `https://drive.google.com/uc?export=view&id=1BqwN4ogQLHim_MOIVPUgwoiyupdSvo6l`
- **Time Period:** January 2011 – November 2024  
- **Format:** Parquet files, organized by year and month.

---

## 🔄 Project Pipeline

### 1. 🧾 Data Ingestion & Aggregation with PySpark
- A `SparkSession` is initialized with optimized memory settings.
- Monthly Parquet files for each year are read into Spark DataFrames.
- DataFrames are unioned by year, then combined into a single full dataset.

### 2. 🧹 Data Cleaning & Preprocessing
- **Column Pruning:** Drop unnecessary columns like `store_and_fwd_flag`, `payment_type`, `mta_tax`.
- **Data Filtering:** Remove trips with invalid values (zero/negative fare or distance, missing timestamps).
- **Sampling:** Take a random 80% sample for efficient training.
- **Null Handling:** Fill null `passenger_count` with a placeholder.

### 3. 🧠 Time Series Feature Engineering
- Aggregate raw trip data into **hourly time series**:
  - `trip_count`: total number of trips
  - `total_revenue`: total amount
  - `total_distance`: trip distance
- Convert Spark DataFrame to pandas for modeling.
- Extract time-based features: hour, day, weekday, month, quarter, year.

### 4. 📊 Exploratory Data Analysis (EDA)
- **Long-Term Trends:** Rolling mean plots (30-day and 720-hour) to show demand trends.
- **Yearly Breakdown:** Zoom in on individual years for seasonal analysis.

### 5. ⚙️ Forecasting with XGBoost
- Gradient boosting used to predict `trip_count` by hour.
- **Features:** Time-based features (hour, weekday, etc.)
- **Split:** 2011–2018 for training, 2019–2020 for testing.
- **Tuning:** Grid search for `max_depth`, `learning_rate`, etc.
- **Evaluation:**
  - Feature importance plot
  - Predictions vs. actual values
  - RMSE and performance by hour/day/month

### 6. 🧠 Forecasting with LSTM (PyTorch)
- **Sequence Input:** 24-hour lookback to predict next hour’s demand.
- **Scaling:** Normalize data with `MinMaxScaler`.
- **Model Architecture:**
  - 1 LSTM layer
  - 1 Fully connected output layer
- **Training:** 20 epochs, Adam optimizer, MSE loss.
- **Evaluation:**
  - RMSE metric
  - Actual vs. predicted plots
