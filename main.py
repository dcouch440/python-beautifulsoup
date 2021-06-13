from bs4 import BeautifulSoup
# first is the file to read, second is the method to use after the file is open

with open('home.html', 'r') as html_file:
  content = html_file.read()

  soup = BeautifulSoup(content, 'lxml')
  course_cards = soup.find_all('div', class_='card')
  for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text.split()[-1]
    # f promotes string interpolation
    print(f'{course_name} costs {course_price}')