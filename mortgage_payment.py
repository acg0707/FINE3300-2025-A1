# ---------------------------------------------------------
# FINE 3300 - Assignment 1 (Part 1)
# Author: Aaditya Chandra Gupta
# Description: Mortgage Payment Calculator
# ---------------------------------------------------------

# Formula Reference:
# PVA(r, n) = (1 - (1 + r) ** -n) / r
# Payment = Principal / PVA(r, n)

class MortgagePayment:
    def __init__(self, annual_rate, amort_years):
        # Mortgage rates in Canada are quoted as semi-annually compounded
        self.annual_rate = annual_rate / 100   # Convert to decimal
        self.amort_years = amort_years

    def payments(self, principal):
        """
        Returns a tuple containing:
        (monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly)
        """

        # Convert semi-annual rate to effective annual rate
        eff_annual_rate = (1 + self.annual_rate / 2) ** 2 - 1

        # Define payment frequencies and corresponding periods per year
        freq = {
            'monthly': 12,
            'semi_monthly': 24,
            'bi_weekly': 26,
            'weekly': 52
        }

        payments = {}

        for key, periods_per_year in freq.items():
            r = (1 + eff_annual_rate) ** (1 / periods_per_year) - 1  # periodic rate
            n = amort_years * periods_per_year                        # total periods
            PVA = (1 - (1 + r) ** -n) / r
            payment = principal / PVA
            payments[key] = round(payment, 2)

        # Accelerated versions use fractions of monthly payments
        payments['rapid_bi_weekly'] = round(payments['monthly'] / 2, 2)
        payments['rapid_weekly'] = round(payments['monthly'] / 4, 2)

        # Return as tuple
        return (
            payments['monthly'],
            payments['semi_monthly'],
            payments['bi_weekly'],
            payments['weekly'],
            payments['rapid_bi_weekly'],
            payments['rapid_weekly']
        )


# ---- Program Execution ----
if __name__ == "__main__":
    print("---- Mortgage Payment Calculator ----")

    # Collect user input
    principal = float(input("Enter the mortgage principal amount ($): "))
    annual_rate = float(input("Enter the quoted annual interest rate (%): "))
    amort_years = int(input("Enter the amortization period (years): "))

    # Create class object
    mortgage = MortgagePayment(annual_rate, amort_years)
    results = mortgage.payments(principal)

    # Display formatted output
    labels = [
        "Monthly Payment",
        "Semi-monthly Payment",
        "Bi-weekly Payment",
        "Weekly Payment",
        "Rapid Bi-weekly Payment",
        "Rapid Weekly Payment"
    ]

    print("\n---- Payment Schedule ----")
    for label, amount in zip(labels, results):
        print(f"{label}: ${amount:,.2f}")
