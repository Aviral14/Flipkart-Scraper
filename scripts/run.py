import scrapy
from scrapy.crawler import CrawlerProcess
import re
import sys
import pickle


class My_Spider(scrapy.Spider):
    """A Class to represent the spider"""

    name = 'spider_final'
    start_urls = [
        'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
    count = 0
    page_number = 1
    css_selector = ''

    @staticmethod
    def check_bounds(response):
        """Function to check whether a valid number of laptops has been entered or not."""

        if max_laptops <= 0:
            print('Please Enter a Valid Number Of Laptops')
            print('Terminating the program! Try Again')
            pickle_out.close()
            sys.exit()

        total_laptops_str = response.css('span._2yAnYN::text').extract()
        regex_obj = re.compile(r' \d+ ')
        total_laptops = int(regex_obj.findall(str(total_laptops_str))[2])

        if max_laptops > total_laptops:
            print('These many laptops not available')
            print('Please enter a number less than '+str(total_laptops))
            print('Terminating the program! Try Again')
            pickle_out.close()
            sys.exit()

    def parse(self, response):
        """Function to parse the data on the webpage."""

        My_Spider.check_bounds(response)

        codes = response.css('div._1-2Iqu.row')

        for code in codes:

            laptop_name = code.css('div._3wU53n::text').extract()
            laptop_rating = code.css('div.hGSR34::text').getall()
            laptop_selling_price = code.css(
                'div._1vC4OE._2rQ-NK::text').extract()

            if laptop_rating == []:
                laptop_rating = ['Unrated']

            My_Spider.count += 1

            pickle.dump({'Laptop Name: ': laptop_name,
                         'Laptop Rating: ': laptop_rating,
                         'Laptop Selling Price: ': laptop_selling_price},
                        pickle_out)

            if(My_Spider.count == max_laptops):
                pickle_out.close()
                sys.exit()

        if My_Spider.count < max_laptops:
            My_Spider.page_number += 1

            if My_Spider.page_number == 2:
                My_Spider.css_selector = 'a._3fVaIS'
            else:
                My_Spider.css_selector = 'a._3fVaIS:nth-child(12)'
            next_page = response.css(
                My_Spider.css_selector+'::attr(href)').get()

            yield response.follow(next_page, callback=self.parse)


def main():
    """The Main Function"""

    global max_laptops
    global pickle_dir
    global pickle_out

    max_laptops = int(sys.argv[1])
    pickle_dir = sys.argv[2]

    pickle_out = open(pickle_dir, 'wb')

    process = CrawlerProcess(
        {'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
    process.crawl(My_Spider)
    process.start()

    pickle_out.close()


main()
