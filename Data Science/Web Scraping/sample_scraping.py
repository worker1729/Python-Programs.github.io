from bs4 import BeautifulSoup
import requests
import csv

url = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
#print(url)

soup = BeautifulSoup(url.content, "lxml")
"""job_titles = soup.find_all("h3", class_="joblist-comp-name")
skills = soup.find_all("span", class_="srp-skills")
for title in a:
    print("Company name: " + title.text)
for title2 in b:
    print("Skills required: " + title2.text.replace(" ",""))
"""
job_titles = soup.find_all("h3", class_="joblist-comp-name")
skills = soup.find_all("span", class_="srp-skills")
for title, skill in zip(job_titles, skills):
    print("Company name: {} Skills required: {}".format(title.text, skill.text.replace(" ","")))


with open('jobs.csv', 'w', newline='') as csvfile:
    fieldnames = ['Company name', 'Skills required']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for title, skill in zip(job_titles, skills):
        writer.writerow({'Company name': title.text, 'Skills required': skill.text.replace(" ","")})