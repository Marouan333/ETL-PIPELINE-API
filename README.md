# ETL Pipeline with Python & SQL

## Overview
This project implements an **ETL (Extract, Transform, Load)** pipeline using **Python** and **SQL**. The pipeline extracts cryptocurrency market data from the **CoinGecko public API**, processes the data by cleaning, transforming, and handling missing values, and loads it into a **Microsoft SQL Server** database for further analysis. This pipeline is automated using a batch file and scheduled to run periodically via **Windows Task Scheduler**.

## Technologies Used
- **Python**:
  - `requests` – For making API requests to CoinGecko
  - `pandas` – For data manipulation, cleaning, and transforming
  - `pyodbc` & `SQLAlchemy` – For connecting to and interacting with Microsoft SQL Server
- **SQL**: **Microsoft SQL Server** – For storing the cleaned data
- **Batch File**: Used to automate running the Python script
- **Windows Task Scheduler**: For scheduling the batch file to run at specified intervals

## Why This Project?

The main goal of this project is to automate the process of fetching, cleaning, and storing cryptocurrency data, ensuring that this information is available in a structured database for further analysis, reporting, or application use. This project demonstrates the use of an ETL pipeline and automating tasks to reduce manual intervention.

## Table of Contents
1. [Installation Steps](#installation-steps)
2. [How it Works](#how-it-works)
3. [Project Motivation](#project-motivation)
4. [Limitations & Challenges](#limitations--challenges)
5. [Intended Use](#intended-use)
6. [Credits](#credits)

## Installation Steps

### Prerequisites
- **Python 3.x** installed on your system.
- A **Microsoft SQL Server** instance running and a database created for storing the data.
- **CoinGecko API** key (optional, based on usage limits).

### Steps to Set Up
1. **Clone this repository**:
   ```bash
   git clone https://github.com/<your-username>/etl-pipeline-python-sql.git
Install the required Python libraries:

bash
Copier
Modifier
pip install -r requirements.txt
Database Setup:

Create a database in Microsoft SQL Server (e.g., COINS).
Ensure the server and database details are correctly configured in the Python script (etl_pipeline.py).
Batch Script Configuration:

Create a batch file (e.g., run_etl.bat) that runs the Python ETL script. Example content of the batch file:
bash
Copier
Modifier
python etl_pipeline.py
Windows Task Scheduler:

Schedule the batch file to run at your desired interval (e.g., daily or hourly).
How it Works
Extract
The extract() function sends an HTTP request to the CoinGecko API to fetch the top 10 cryptocurrencies' market data (e.g., market cap, volume, and current price). The data is returned in JSON format.

Transform
The transform() function processes the extracted data by:

Selecting relevant columns (e.g., CoinID, Symbol, CoinName, etc.).
Renaming columns for better readability.
Converting the timestamp to a proper datetime format.
Handling missing data by filling missing values with 0 for price, market cap, and volume.
Load
The load() function stores the transformed data into a Microsoft SQL Server database. It writes the data into the BTC table, replacing any existing records.

Automation
The entire ETL process is automated using a batch file, which is scheduled to run periodically using Windows Task Scheduler. This ensures that the data is updated automatically at the specified intervals.

Project Motivation
The idea behind this project came from the need to automate the collection and storage of cryptocurrency market data in a structured database for easy access and analysis. As cryptocurrency data changes frequently, having an automated process to regularly update this information helps businesses or researchers maintain up-to-date data without manual intervention.

Limitations & Challenges
API Rate Limits: CoinGecko has rate limits, which may limit the frequency of data extraction if you're using a free API key.
Data Quality: While the data is extracted from a reputable source, there could still be some missing or incomplete data, which is handled during the transformation step.
Server Configuration: The pipeline requires proper configuration of the SQL Server instance, which could pose difficulties if the database settings are not correctly configured.
Intended Use
This project is intended for anyone looking to automate the collection of cryptocurrency market data and store it in a SQL database for further analysis, reporting, or other use cases. It is particularly useful for businesses, data analysts, or developers who require real-time data for decision-making or applications.

Credits
CoinGecko for providing a free and reliable API for cryptocurrency data.
Microsoft SQL Server for managing the database.
Python Libraries (requests, pandas, pyodbc, SQLAlchemy) for their functionality in handling data extraction, transformation, and database interaction.
Windows Task Scheduler for enabling automation of the ETL pipeline.
