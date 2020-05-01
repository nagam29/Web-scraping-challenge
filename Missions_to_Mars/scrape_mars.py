
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
    browser.visit(url)
    import time
    time.sleep(15)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())
    # text of mars weather is between span tags. So, just find all the text related to span tags
    # text of mars weather is between span tags. So, just find all the text related to span tags
    #soup2 = bs(html)
    weather_report=[]
    for span_tag in soup.find_all('span'):
        if 'sol' in span_tag.text:
            weather_report.append(span_tag.text) 
        ### print("Found span text:", span_tag.text)
    ### print(weather_report[0])

    # there are a few mars weathers are posted. Let's save one
    mars_weather=weather_report[0]
    ### print(mars_weather)
    scraped["weather"] = mars_weather

    # Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    ### tables
    # Keep the first table in data frame
    df=tables[0]
    ### print(df)
    df2=df.iloc[:]
    ### df2
    df2.columns = ['description','value']
    # set description as index
    df2.set_index('description', inplace=True)
    ### df2
    # Convert it to html
    html_table = df2.to_html()
    ### html_table
    # Remove \n
    mars_fact_html=html_table.replace('\n', '')
    ### mars_fact_html
    scraped["fact"] = mars_fact_html
    
    # Mars Hemispheres

    # Cerberus Hemisphere
    url_cer = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_cer)
    time.sleep(15)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())

    for result in soup:
        try:
            title=result.find('h2', class_="title").text
            link=result.find_all('a',href="http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg")
        
            ###if (title and link):
                ### print(title)
                ### print(link)
        except AttributeError as e:
            print(e)

        title_cer=title
        link_cer=link
        ### print(title_cer,link_cer)

    # Schiaparelli Hemisphere

    url_shi = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_shi)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())
    for result in soup:
        try:
            title=result.find('h2', class_="title").text
            link=result.find_all('a',href="http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg")
            
            ### if (title and link):
                ### print(title)
                ### print(link)
        except AttributeError as e:
            print(e)

        title_schi=title
        link_schi=link
        ### print(title_schi,link_schi)

    # Syrtis Major Hemisphere

    url_syr = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_syr)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())

    for result in soup:
        try:
            title=result.find('h2', class_="title").text
            link=result.find_all('a',href="http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg")
            
           ###  if (title and link):
                ### print(title)
                ### print(link)
        except AttributeError as e:
            print(e)

        title_syr=title
        link_syr=link
        ### print(title_syr,link_syr)

    # Valles Marineris Hemisphere 
    url_val = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_val)
    time.sleep(10)
    html = browser.html
    soup = bs(html, 'html.parser')
    ### print(soup.prettify())

    for result in soup:
        try:
            title=result.find('h2', class_="title").text
            link=result.find_all('a',href="http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg")
            
            ### if (title and link):
                ### print(title)
                ### print(link)
        except AttributeError as e:
            print(e)

        title_val=title
        link_val=link
        ### print(title_val,link_val)

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    ]
    ### print(hemisphere_image_urls)

    return (scraped,hemisphere_image_urls)
    
print(scrape())