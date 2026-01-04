# python_beginner_mt
Extract Product Data - Educational Purpose

### Product Price Scraper (Beginner Python Project) ###
## Project Overview

This project is a Python web scraping application that extracts product names and prices from the City Mall Myanmar website and saves the data into an Excel file with a timestamp.

It is designed as a Beginner Final Project to practice:
* HTTP requests
* HTML parsing
* Data cleaning
* Working with Pandas
* Exporting data to Excel

## Features
* Sends browser-like HTTP requests using requests
* Implements retry strategy for stable scraping
* Parses HTML using BeautifulSoup
* Extracts:
    Product Name
    Product Price (Normal & Sale price)
* Cleans price data (removes symbols and commas)
* Saves extracted data to an Excel (.xlsx) file
* Auto-generates timestamped filenames

## Technologies & Libraries Used
* Python
* requests
* beautifulsoup4
* html5lib
* pandas
* urllib3
* datetime

## Project Structure
Beginner_Final_Project/
│
├── scraper.py          # Main Python script
├── README.md           # Project documentation
└── Extracted Data *.xlsx  # Output Excel files (generated)

## Installation & Setup
* Clone the Repository
git clone https://github.com/your-username/citymall-price-scraper.git
cd citymall-price-scraper

* Install Required Libraries
pip install requests pandas beautifulsoup4 html5lib urllib3

* How to Run the Project
python scraper.py


After running:
* The program will scrape product data
* An Excel file will be generated automatically
Example:
Extracted Data 14-35-20.xlsx

## Output Example
Product Name	Product Price
Product A	3500
Product B	12000

## Notes & Limitations
* Website structure changes may break the scraper
* This project is for educational purposes only
* Avoid sending too many requests to prevent blocking
* Prices are stored as integers (MMK)

## Learning Outcomes
* By completing this project, you will understand:
* How web scraping works
* How to handle HTTP errors and retries
* Data extraction and cleaning
* Converting scraped data into Excel files
* Writing structured Python programs

## Author
Myo Thant
Beginner Python Learner

## License
This project is open-source and intended for learning and educational use.
