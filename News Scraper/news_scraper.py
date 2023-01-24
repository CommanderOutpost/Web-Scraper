from bs4 import BeautifulSoup
import requests
import time
import json
import subprocess

def get_page(url, tag, class_name):
    response = requests.get(url)
    html_page = response.text

    soup  = BeautifulSoup(html_page, 'html.parser')
    heading_text = ""

    for heading in soup.find_all(tag, class_ = class_name):
        heading_text += heading.text
        heading_text += "\n\n"

    return heading_text

def add_to_file(page_info, format):
    if format == "json":
        json_str = json.dumps(page_info)
        with open("news_data.json", "w") as file:
            file.write(json_str)
        print(json_str)
    elif format == "txt":
        with open("news_data.txt", "w") as file:
            file.write(page_info)
    else:
        print("Invalid format. Please choose between json or txt")

def read_past_text(file, format):
    if format == "json":
        with open(file, "r") as file:
            data = json.load(file)
        print(data)
    elif format == "txt":
        with open(file, "r") as file:
            data = file.read()
        print(data)
    else:
        print("Invalid format. Please choose between json or txt")

def convert_time():
    time_type = input("What time type do you want? (minute, hour, or second): ")
    time_input = int(input("Enter the time: "))
    if time_type == "second":
        return time_input
    elif time_type == "minute":
        return time_input * 60
    elif time_type == "hour":
        return time_input * 60 * 60
    else:
        print("Invalid time type. Please choose between minute, hour, or second.")


url = input("Enter the url: ")
tag = input("Enter the tag you want to scrape: ")
class_name = input("Enter the class name: ")
format = input("Enter the format the file should be saved in (json or txt): ").lower()
time_ = convert_time()


while True:
    page_info = get_page(url, tag, class_name)
    print(page_info)
    add_to_file(page_info, format)
    subprocess.run(['notify-send', "News Scraping", "News today has successfully been scraped"])
    time.sleep(time_)


