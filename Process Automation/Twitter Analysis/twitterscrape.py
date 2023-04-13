import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

users = []
i = 0

browser.get("https://twitter.com/LaboonSocial/followers")
while i < 30:
    time.sleep(2)

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    html=browser.page_source
    soup=BeautifulSoup(html)
    usernames=soup.find_all('a',class_="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l")
    time.sleep(2)
    for j in usernames:
        users.append(j.text)
    
    i=i+1

df = pd.DataFrame(users, columns = ["Users"])
df.to_csv("twitterfollowers.csv")
print(users)