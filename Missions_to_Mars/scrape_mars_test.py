# test
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from selenium import webdriver


def scrape():
    scraped={}
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/8654/how-nasas-perseverance-mars-team-adjusted-to-work-in-the-time-of-coronavirus/'
    # Request the page, Retrieve the page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    ### print(soup.prettify())
    # Collect the latest News Title
    news_title = soup.find('h1',{"class":"article_title"}).text
    # Add the latest new title to the dictionary
    scraped["news_t"] = news_title.replace('\n',' ')

    # Get the first paragraph
    # reference https://www.studytonight.com/python/web-scraping/find-tags-with-beautifulsoup
    p_tags=soup.find_all('p')
    ### print(p_tags)
    # Get "<p><i>Like much of the rest of the world, the Mars rover team is pushing forward with its mission-critical work while putting the health and safety of their colleagues and community first.</i></p>"
    # This sentence is the second item in the list
    for tag in p_tags:
        try:
            news_p=tag.find('i').text
            ### if (news_p):
                ### print(news_p)
        except AttributeError:
            pass
    scraped["news_parag"]=news_p

    # JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': 'c:/webdrivers/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA23852'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())
    results=soup.find_all('article')
    ### results
    featured_image_url='https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23852_hires.jpg'
    scraped["feature_img"] = featured_image_url

    # Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    #url = 'https://twitter.com/MarsWxReport/status/1254875768108331008'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())
    # text of mars weather is between span tags. So, just find all the text related to span tags
    soup2 = bs(html)
    for span_tag in soup2.find_all('span'):
        print(span_tag.text)
        mars_weather_temp=span_tag.text
        # there are a few mars weathers are posted. Let's save one
        mars_weather='InSight sol 503 (2020-04-26) low -93.8ºC (-136.8ºF) high -4.9ºC (23.2ºF) winds from the WNW at 4.6 m/s (10.2 mph) gusting to 17.5 m/s (39.1 mph) pressure at 6.70 hPa'
        print(mars_weather)

    scraped["weather"] = mars_weather

    return scraped

print(scrape())