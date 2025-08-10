"""
Lab15_Bgyeduaa1.py
Author: Belinda Gyeduaa
Purpose: Read and analyze unemployment rate data from 'OHURN.csv', 
then plot the national unemployment rate over time.
Date: 08/09/2025
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def main():
    filename = 'OHURN.csv'

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        # Analyze header with enumerate()
        print("Header information with index:")
        for index, header in enumerate(headers):
            print(f"{index}: {header}")

        dates = []
        unemployment_rates = []

        for row in reader:
            date_str = row[0]
            rate_str = row[1]

            # Convert date string to datetime object (format: YYYY-MM-DD)
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                rate = float(rate_str)
            except ValueError:
                # Skip rows with invalid data
                continue

            dates.append(date)
            unemployment_rates.append(rate)

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(dates, unemployment_rates, marker='o', linestyle='-', color='b')
    plt.title('National Unemployment Rate Over Time')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
