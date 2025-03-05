import requests
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

def extract():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code, response.text)
        return None

def transform(data):
    if not data:
        print("No data to transform.")
        return pd.DataFrame()
    
    df = pd.DataFrame(data)

    # Selecting relevant columns
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'last_updated']]

    # Renaming columns
    df.rename(columns={
        'id': 'CoinID',
        'symbol': 'Symbol',
        'name': 'CoinName',
        'current_price': 'PriceUSD',
        'market_cap': 'MarketCap',
        'total_volume': 'Volume',
        'last_updated': 'Timestamp'
    }, inplace=True)

    # Convert 'Timestamp' to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Fill missing values
    df.fillna({'PriceUSD': 0, 'MarketCap': 0, 'Volume': 0}, inplace=True)
    
    return df

def load(df):
    if df.empty:
        print("No data to load.")
        return
    
    server = r'delllll\SQLEXPRESS'
    database = 'COINS'
    driver = 'ODBC Driver 17 for SQL Server'
    
    connection_string = f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver={driver}"
    engine = create_engine(connection_string)
    
    # Exclude 'Timestamp' if it's an auto-generated column in SQL Server
    df = df.drop(columns=['Timestamp'], errors='ignore')
    
    # Write DataFrame to SQL Server
    df.to_sql("BTC", engine, if_exists="replace", index=False)
    print("Data successfully loaded into COINS Database")

# Run ETL Pipeline
data = extract()
df_cleaned = transform(data)
load(df_cleaned)
