# FINE3300-2025-A1
Python assignment for FINE 3300: Mortgage Payment and Exchange Rate calculator

FINE 3300 (Fall 2025) — Assignment #1
Author: Aaditya Chandra Gupta
Schulich School of Business | York University

Overview

This repository contains both parts of Assignment #1 for the course FINE 3300 (Fall 2025).
The assignment focuses on using Python and Visual Studio Code, while managing version control through GitHub.

The project includes:

1. Mortgage Payment Calculator — Computes different types of Canadian mortgage payment frequencies.
2. Currency Exchange Converter — Reads exchange rate data from a CSV file (Bank of Canada) and converts between CAD and USD.

Part 1: Mortgage Payments
Description: 
The MortgagePayment class calculates the periodic payments for various payment frequencies:
- Monthly
- Semi-monthly
- Bi-weekly
- Weekly
- Rapid Bi-weekly
- Rapid Weekly

The program uses the present value of annuity formula:

PVA(r,n)= (1−(1+r)^−n)/r

where:
r = periodic interest rate
n = total number of payment periods

Fixed-rate mortgage rates in Canada are semi-annually compounded, so the effective annual rate is converted accordingly before computing payments.

How to Run
Open your terminal or VS Code integrated terminal.
Navigate to your cloned repository folder:
cd FINE3300-2025-A1

Run the script:
python mortgage_payment.py

Enter:
- Principal amount ($)
- Quoted annual interest rate (%)
- Amortization period (years)

Example Input & Output

Input:
Principal: $500000  
Interest Rate: 5.5%
Amortization: 25 years

Output:
Monthly Payment: $3,051.96  
Semi-monthly Payment: $1,524.25  
Bi-weekly Payment: $1,406.88 
Weekly Payment: $703.07
Rapid Bi-weekly Payment: $1,525.98  
Rapid Weekly Payment: $762.99


Part 2: Exchange Rates
Description
The ExchangeRates class reads Bank of Canada’s Exchange Rate CSV file (BankOfCanadaExchangeRates.csv) using pandas.
It identifies the latest USD/CAD rate (last row of the dataset) and allows users to convert between the two currencies.

How It Works
- Reads the CSV file automatically from the same directory as the Python script.
- Extracts the last row to obtain the most recent USD/CAD exchange rate.
- Performs conversion based on user input using:
    - USD → CAD: amount * rate
    - CAD → USD: amount / rate

How to Run
Make sure the following files are in the same directory:
exchange_rates.py
BankOfCanadaExchangeRates.csv

Run the script:
python exchange_rates.py

Enter:
- Amount
- “From” currency (USD or CAD)
- “To” currency (USD or CAD)

Example Input & Output

Input:
Enter amount: 100000  
Convert from: USD  
Convert to: CAD

Output: 
100,000.00 USD = 136,980.00 CAD


Reverse Conversion: 
Enter amount: 100000  
Convert from: CAD  
Convert to: USD

Output
100,000.00 CAD = 73,003.36 USD

Files Included: 
1. mortgage_payment.py	Mortgage payment calculator (Part 1)
2. exchange_rates.py	Exchange rate converter (Part 2)
3. BankOfCanadaExchangeRates.csv	CSV file with exchange rates
4. README.md	This documentation file

Repository link: https://github.com/acg0707/FINE3300-2025-A1
