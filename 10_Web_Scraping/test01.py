import time

from selenium import webdriver

my_portfolio = [
        {"Name": "LUKA DONČIĆ" ,
         "Type": "Assist",
         "Date": "1/17/2021",},        

        {"Name": "JAMYCHAL GREEN",
         "Type": "Dunk",
         "Date": "1/3/2021",},        

        {"Name": "T.J. MCCONNELL",
         "Type": "Assist",
         "Date": "12/23/2020",},

]  

driver = webdriver.Chrome("./chromedriver_WIN_111_0_5563_65.exe")
driver.get("https://livetoken.co/listings/topshot")

time.sleep(5)
driver.close()