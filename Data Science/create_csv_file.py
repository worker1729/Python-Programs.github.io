from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get("url_address")
#print(url)

#In the code below is found the information used in the variable called "text".
soup = BeautifulSoup(url.content, "lxml")
a = soup.find_all("tag_name", class_="class_name")
for x in a:
    print(x.text.strip())

#Create the first column and new CSV file.
data = []
for x in a:
    data.append([x.text.strip()])
df = pd.DataFrame(data, columns=['Column_name'])
df.to_csv("file_name.csv", index=False)

