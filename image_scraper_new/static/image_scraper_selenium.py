from selenium import webdriver
import time
import string
import random

import traceback

class MyHouseSpider():
    name = "my-house-spider"
    start_urls = ["https://www.google.com/"]
    number_of_pictures_to_scrape = 10
    def parse(self):
        print "#############################Google Image Scraper VERSION 1##############################"

        #Add the list of Search terms to this array
        city_urls = ["Snooze","Parma Cucina Italiana","Eddy V's Prime Seafood","Hodad's","Oceana Coastal Kitchen","CUCINA urbana","A.R. Valantien's at the Lodge at Torrey Pines","Truluck's Seafood Steak and Crab","Cottage","Sushi Ota","The Baked Bear","Kono's Cafe","Blue Water Seafood Market & Grill","Hash House a Go Go","Phil's BBQ","Juniper and Ivy","Island Prime Restaurant","Richard Walker's Pancake House","Seasons 52","The Mission Restaurant","Piatti","Mitch's Seafood","Civico 184","Stone Bistro World Bistro & Gardens"]
        #Opens Selenium and Navigates to google.de
        driver = webdriver.Firefox()
        picture_array = []
        
        #Will loop through the city_urls (search terms)
        for city_number in range(0,len(city_urls)):
            i = 1
            time.sleep(random.randrange(0,1,5))
            search_string = string.replace(city_urls[city_number], '-', '+')
            driver.get("https://www.google.com/search?q=" + search_string + " San+Diego&tbs=isz:lt,islt:vga&tbm=isch")
            while i < self.number_of_pictures_to_scrape:
                try:
                    #driver.get("https://www.google.com/search?q=" + search_string + " beach+Homes&tbs=isz:lt%2Cislt:4mp&tbm=isch")
                    #Gets the URL of Image x
                    picture_url = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[2]/div[3]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div[1]/div[" +str(i) +"]/a").get_attribute("href")
                    #Clears the google path to give clean Image URL Path
                    picture_url = picture_url.split('http://images.google.de/imgres?imgurl=', 1)[1]
                    picture_url = picture_url.split('&imgrefurl', 1)[0]
                    print picture_url
                    picture_array.append(picture_url)
                    #Sends the URL to Scrapy to crawl and download
                    #yield HousePicture(image_urls=[picture_url], my_nice_file_name=city_urls[city_number])
                    i = i + 1
                except:
                    traceback.print_exc()
                    i = i + 1
                    
#pic = MyHouseSpider()
#pic.parse()
                    #[line.rstrip('\n') for line in open('./static/date')]

city_urls = ["Snooze","Parma Cucina Italiana","Eddy V's Prime Seafood","Hodad's","Oceana Coastal Kitchen","CUCINA urbana","A.R. Valantien's at the Lodge at Torrey Pines","Truluck's Seafood Steak and Crab","Cottage","Sushi Ota","The Baked Bear","Kono's Cafe","Blue Water Seafood Market & Grill","Hash House a Go Go","Phil's BBQ","Juniper and Ivy","Island Prime Restaurant","Richard Walker's Pancake House","Seasons 52","The Mission Restaurant","Piatti","Mitch's Seafood","Civico 184","Stone Bistro World Bistro & Gardens"]
city_strip = [city.replace("'", "").replace(" ", "_") for city in city_urls]
print city_strip
