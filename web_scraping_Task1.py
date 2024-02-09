import bs4
import requests
from cleantext import clean 
import schedule
import time
"""
This web_scraping script will be taking any link as input and process it according to scrap_data function created,with only the
information of the headline called out of the web-site
"""
def scrap_data():    
"""
This is the function that takes a link as input for flexebility, and multiple link assignment, please pass any link as input 
to scrap data, the function makes request to get the information of the web-site passed by its link
"""
 website_link = str(input("Enter link:"))
 res = requests.get(website_link)
 print("The object type:",type(res))
 soup = bs4.BeautifulSoup(res.text,'html5lib')
 print("The object type:", type(soup))
 soup.select('.mw-headline')
 for i in soup.select('.mw-headline'):
    print(i.text,end=',')

"""
Cleaning data by removing Html tags, removing unwanted char, normalizing text, handling concatination
"""
raw_text = scrap_data()  
clean_text = clean(raw_text, clean_special_chars=True,lowercases=True, replace_with_contractions=True, clean_non_text = True)
print(clean_text)

"""
scheduling that the script will be running every wednesday at 12:00 noon to scrap any data that is with
respect to any link of web-site passed to it 
"""
schedule.every().wednesday.at("12:00").do(scrap_data) #The script will be running every Wednesday at 12:00 midday

"""
looping the time schedule 
"""
while 1: 
  schedule.run_pending()
  time.sleep(1)

     
    



