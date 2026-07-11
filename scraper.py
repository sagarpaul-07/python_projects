import requests
import random
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog/"
random_number = random.randint(1, 9999999)
response = requests.get(url, headers = {'user-agent': f'{random_number}'})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article')

for blog in blogs:
    title = blog.find('h2').text.strip()
    print(f'Title: {title}')

    blog_datetime_string = blog.find('time', class_='entry-time').get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime.strftime("%A %B %d, %Y at %I:%M %p")

    print(f"Date: {pretty_date}")