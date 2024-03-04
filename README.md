# Cryptocurrency Data from Binance API

This project retrieves historical cryptocurrency price data from the Binance API and saves it to a CSV file.

## Requirements

- **Python Version:** Python 3.x
- **Required Libraries:** `requests`, `pandas`


## Configuration
- **Cryptocurrencies:** Modify the coins list to include the symbols of the cryptocurrencies you want to fetch.
- **Data Interval:** Adjust the interval variable to set the data interval ('1h' for 1 hour, '1d' for 1 day, etc.).
- **Data Limit:** Set the limit variable to determine the number of data points to fetch.
- **End Time:** Adjust the endTime variable to specify the end time of the data retrieval period.

## Data Structure

The script fetches historical price data for each specified cryptocurrency and processes it into a DataFrame with the following columns:

- **Date:** The date of the recorded price data.
- **Time:** The time of day when the data was recorded.
- **Open:** The opening price of the cryptocurrency.
- **High:** The highest price reached during the recorded period.
- **Low:** The lowest price reached during the recorded period.
- **Close:** The closing price of the cryptocurrency.
- **Volume:** The trading volume of the cryptocurrency.
- **Symbol:** The symbol or code representing the specific cryptocurrency.

The processed data is then saved to a CSV file named `CryptocurrencyDataBinance.csv`.

## Things to Consider

When working with this project, it's crucial to consider the following important points:

- **API Limitations:** Binance API usage comes with certain limitations. Please refer to the [Binance API documentation](https://binance-docs.github.io/apidocs/spot/en/) to ensure compliance with these limitations.
- **Web Scraping Ethics:** While performing data extraction, carefully read and comply with the usage terms of Binance or other websites. Conduct web scraping in accordance with ethical guidelines.
- **Up-to-Date Components:** Ensure that libraries, API endpoints, and other components used in your project are up-to-date. Outdated libraries or API changes may affect the functionality of your code.

