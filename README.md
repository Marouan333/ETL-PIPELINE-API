Overview
This project implements an ETL (Extract, Transform, Load) pipeline using Python and SQL to automate data extraction from the CoinGecko public API, process and clean the data, and store it in a Microsoft SQL Server database. The pipeline is scheduled using a batch file and Windows Task Scheduler for automation.

Features
Extract: Fetches the top 10 cryptocurrencies' market data from the CoinGecko API.
Transform: Cleans the data, handles missing values, renames columns, and converts timestamps to datetime format.
Load: Loads the cleaned data into a SQL Server database for further analysis.
Automation: The ETL process is automated with a batch script executed through Windows Task Scheduler.
Technologies Used
Python: For scripting and automation
requests (for making API calls)
pandas (for data manipulation and cleaning)
pyodbc & SQLAlchemy (for database connection and interaction)
SQL: For storing and managing data in Microsoft SQL Server
Batch File: For automating the execution of the Python script
Windows Task Scheduler: For scheduling the batch script to run periodically
Project Setup
Prerequisites
Python 3.x installed on your system.
A Microsoft SQL Server instance running, and a database created for storing the data.
A CoinGecko API key (optional, depending on usage limits).
Installation Steps
Clone this repository:

bash
Copier
Modifier
git clone https://github.com/<your-username>/etl-pipeline-python-sql.git
Install the required Python libraries:

bash
Copier
Modifier
pip install -r requirements.txt
Database Setup:

Create a database in Microsoft SQL Server (e.g., COINS).
Make sure you configure the server and database details in the script (etl_pipeline.py).
Batch Script Configuration:

Create a batch file (e.g., run_etl.bat) that runs your ETL Python script. Example:
bash
Copier
Modifier
python etl_pipeline.py
Windows Task Scheduler:

Schedule the batch file to run at your desired interval (e.g., daily or hourly).
How it Works
Extract:

The extract() function makes an HTTP request to the CoinGecko API to fetch cryptocurrency data (like market cap, volume, etc.).
Transform:

The transform() function processes the data, renaming columns, converting timestamps, and filling missing values.
Load:

The load() function stores the cleaned data into a Microsoft SQL Server database, replacing any existing records in the BTC table.
Automation:

Once the task is scheduled using Windows Task Scheduler, the batch file will automatically run the Python script at specified intervals.
