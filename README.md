# Automated Book Data Scraper

## Overview
This project demonstrates automated multi-page web scraping using Python, BeautifulSoup, and Pandas.

The scraper extracts:
- Book Title
- Price
- Stock Availability
- Rating

The collected data is cleaned and exported into a structured CSV dataset.

---

## Technologies Used
- Python
- Requests
- BeautifulSoup4
- Pandas

---

## Features
- Multi-page scraping (50 pages)
- Automated data extraction
- CSV export
- Data cleaning
- Structured dataset generation

---

## Output
- 1000 scraped book records
- CSV dataset ready for analysis

---

## Sample Output

| Title | Price | Rating |
|---|---|---|
| A Light in the Attic | 51.77 | Three |

---

## Project Structure

```bash
automated-book-data-scraper/
│
├── webScraping/
│   ├── webScraping.py
│   └── books_data.csv
│
├── README.md
├── LICENSE
└── .gitignore
```
