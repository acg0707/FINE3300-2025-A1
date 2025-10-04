# ---------------------------------------------------------
# FINE 3300 - Assignment 1 (Part 2)
# Author: Aaditya Chandra Gupta
# Description: Currency Exchange Converter using Bank of Canada data
# ---------------------------------------------------------

import pandas as pd

class ExchangeRates:
    def __init__(self, filepath = "BankOfCanadaExchangeRates.csv"):
        # Read the CSV file into a pandas DataFrame
        self.data = pd.read_csv(filepath)
        # Extract the last row (latest exchange rates)
        self.latest = self.data.iloc[-1]
        # Get the USD/CAD exchange rate
        # Get the column named "USD/CAD"
        self.usd_to_cad = float(self.latest["USD/CAD"])

    # Creating the function to convert USD to CAD and vice-versa; also used docstring to explain function purpose
    def convert(self, amount, from_currency, to_currency):
        """
        Converts between CAD and USD using the latest exchange rate.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == "USD" and to_currency == "CAD":
            result = amount * self.usd_to_cad
        elif from_currency == "CAD" and to_currency == "USD":
            result = amount / self.usd_to_cad
        else:
            raise ValueError("Only USD and CAD conversions are supported.")
        
        return round(result, 2)


# ---- Program Execution ----
if __name__ == "__main__":
    print("---- Currency Exchange Converter ----")
    
    # Load exchange rate data
    converter = ExchangeRates("BankOfCanadaExchangeRates.csv")

    # Prompt user input
    amount = float(input("Enter amount: "))
    from_curr = input("Convert from (USD or CAD): ")
    to_curr = input("Convert to (USD or CAD): ")

    # Perform conversion
    try:
        result = converter.convert(amount, from_curr, to_curr)
        print(f"\n{amount:,.2f} {from_curr.upper()} = {result:,.2f} {to_curr.upper()}")
    except ValueError as e:
        print(e)
