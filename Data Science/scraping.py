from bs4 import BeautifulSoup

with open("index.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_="button")
    for x in course_cards:
        course_name = x.h2.text
        course_price = x.button.text.split()[-1]
        print(f'{course_name} costs {course_price}')
        #print(course_price)
    #courses_html_tags = soup.find_all('h2')
    #for course in courses_html_tags:
        #print(course.text)
