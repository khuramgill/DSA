
from selenium import webdriver  
from bs4 import BeautifulSoup  
from selenium.webdriver.chrome.service import Service
import pandas as pd #install chrom webdriver  
#webdriver can be downloaded from  
#https://sites.google.com/chromium.org/driver/downloads/version  
service = Service(executable_path='C:\\Users\\lenovo\\Downloads\\Compressed\\chromedriver-win64\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options) 
  
products=[] #List to store name of the product 
prices=[] #List to store price of the product 
ratings=[] #List to store rating of the product 
driver.get("https://www.flipkart.com/search?q=gaming+laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")

content = driver.page_source  
soup = BeautifulSoup(content)  
# print(soup)  
for a in soup.findAll('div',attrs={'class':'_37K3-p'}): 
     print (a)  
     name=a.find('a', attrs={'class':'s1Q9rs'})     
     price=a.find('div',attrs={'class':'_30jeq3'})   
     rating=a.find('div',attrs={'class':'_3LWZlK'})      
     products.append(name.text)      
     prices.append(price.text) 
     ratings.append(rating.text)  
  
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})   
df.to_csv('products.csv', index=False, encoding='utf-8') 