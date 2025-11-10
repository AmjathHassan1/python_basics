import chromedriver_autoinstaller
from selenium import webdriver

# Automatically install and yse the correct ChromeDriver
chromedriver_autoinstaller.install()


# Initialize the driver
driver = webdriver.Chrome()


# Open a website

driver.get("https://www.example.com")

print("Title", driver.title)


from selenium.webdriver.common.by import By
heading=driver.find_element(By.TAG_NAME,"h1")
print(heading.text)

paragraph=driver.find_element(By.TAG_NAME,"p")
print(paragraph.text)

import csv
with open("output.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title","Paragraph"])
    writer.writerow([heading.text,paragraph.text])

driver.quit()