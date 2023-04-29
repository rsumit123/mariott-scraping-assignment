# Marriott Hotels Scraping Assignment

This is a Python-based web scraper that extracts information about Marriott Hotels. The scraper is built using Scrapy, an open-source and collaborative web crawling framework written in Python.

## Requirements

The following software is required to run the scraper:

- Python 3.10
- Scrapy

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/rsumit123/mariott-scraping-assignment
   ```

2. Go inside the repo

   ```
   cd mariott-scraping-assignment
   ```

3. Open a pipenv shell

   ```
   pipenv shell
   ```



  

2. Install the required packages:

   ```
   pienv install
   ```

## Usage

1. Navigate to the project directory:

   ```
   cd scraping-assignment
   ```

2. Run the scraper:

   ```
   python hotel_scraper.py
   ```

   The scraper will start running and will extract information about hotel urls listed in the code, the csv output of all the mentioned urls can be found inside the `output` folder.

   

## Output

The extracted data will be saved in a CSV file named `hotel_code_data.csv`. The CSV file will contain the following columns:

c

- `checkin`: The checkin time
- `PerNight`: per night time without taxes
- `checkout`: Checkout time
- `roomname`: Roomname
- `checkout`: Checkout time
- `ratename`: Name of the rate ex: Flexible
- `StayTotalwTaxes`: price including taxes
- `currency`: currency
- `availability`: Availability of the room (NA if not present)
- `cancelpolicy`: cancellation policy if mentioned else NA
- `paymentpolicy`: payment policy if mentioned else NA


## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) file for more information.