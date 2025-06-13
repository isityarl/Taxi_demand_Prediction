# NYC Yellow Taxi Trip Count Forecasting

**Forecasting** of New York City's Yellow Taxi trip counts using a large dataset spanning from **2011 to 2024**. Implementation of two models—**XGBoost** and an **LSTM neural network**—to predict **hourly taxi demand**.



The primary goal is to build robust forecasting models that can capture the complex **patterns, trends, and seasonality** in NYC taxi usage over more than a decade.




## Data Source

- **Dataset:** NYC Yellow Taxi Trip Records. Link: `https://drive.google.com/uc?export=view&id=1BqwN4ogQLHim_MOIVPUgwoiyupdSvo6l`
- **Time Period:** January 2011 – November 2024  
- **Format:** Parquet files, organized by year and month.

**Hourly**
![image](https://github.com/user-attachments/assets/4ce05a67-7bb3-4ff8-b44b-091a1bbcc4fa)

**Daily**
![image](https://github.com/user-attachments/assets/11bdf3ce-968b-40ba-8a17-8d6bfcca4e82)


## Results:
  XGBoost's RMSE: 1974.8699
  LSTM's RMSE: 0.0095

XGBOOST couldn't handle COVID event, so used `2011-2019` 
  
**XGBOOST actual vs predicted** `mean hour in a day`
![image](https://github.com/user-attachments/assets/74baebe1-5758-4c63-9415-19aa2496eb05)

**XGBOOST actual vs predicted**
![image](https://github.com/user-attachments/assets/0aa087f5-f0dc-4b54-b143-ebbc7416774c)

For LSTM full `2011-2024` 

**LSTM actual vs predicted** 
![image](https://github.com/user-attachments/assets/d2912389-b02c-4a77-90d5-ef10176e16f1)

