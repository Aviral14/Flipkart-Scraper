# Flipkart-Scraper
A script to scrape laptop infromation from flipkart website using Scrapy

Use run.py script to scrape the flipkart website for laptops.
Type -

python3 run.py 'no. of laptops to be scraped' 'name of file used to store data'

[Example- python3 run.py 400 pickle_file]
in the terminal to run the script.
The number of laptops entered must be between 0 and the total number of laptops listed on the website.

To display the data scraped from the website use the retrieve.py script.
Type -

python3 retrieve.py 'file in which data is stored'.

in the terminal to run this script.
