# ETL Pipeline with Python & SQL

## Overview
This project implements an **ETL (Extract, Transform, Load)** pipeline using **Python** and **SQL** to automate data extraction from the **CoinGecko public API**, process and clean the data, and store it in a **Microsoft SQL Server** database. The pipeline is scheduled using a batch file and Windows Task Scheduler for automation.

## Features
- **Extract**: Fetches the top 10 cryptocurrencies' market data from the CoinGecko API.
- **Transform**: Cleans the data, handles missing values, renames columns, and converts timestamps to datetime format.
- **Load**: Loads the cleaned data into a SQL Server database for further analysis.
- **Automation**: The ETL process is automated with a batch script executed through Windows Task Scheduler.

## Technologies Used
- **Python**: For scripting and automation
  - `requests` (for making API calls)
  - `pandas` (for data manipulation and cleaning)
  - `pyodbc` & `SQLAlchemy` (for database connection and interaction)
- **SQL**: For storing and managing data in **Microsoft SQL Server**
- **Batch File**: For automating the execution of the Python script
- **Windows Task Scheduler**: For scheduling the batch script to run periodically

## Project Setup

### Prerequisites
- **Python 3.x** installed on your system.
- A **Microsoft SQL Server** instance running, and a database created for storing the data.
- A **CoinGecko API** key (optional, depending on usage limits).

### Installation Steps

1. **Clone this repository**:
   ```bash
   git clone https://github.com/<your-username>/etl-pipeline-python-sql.git
