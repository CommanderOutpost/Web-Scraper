# Web-Scraper
This code is a web scraping script that uses the BeautifulSoup library to scrape a specified website, retrieve specified HTML tags and class names, and save the retrieved information to a file. The script prompts the user for a website URL, an HTML tag, a class name, and a file format (either "json" or "txt").

The script defines several functions:

* The get_page() function takes in a URL, an HTML tag, and a class name as arguments, and uses the requests library to send a GET request to the specified URL. It then uses BeautifulSoup to parse the HTML content of the page and find all instances of the specified tag and class name. The text content of each element found is concatenated and returned as a string.

* The add_to_file() function takes in the scraped page information and the specified file format, and writes the information to a file. If the format is "json", the information is first converted to a JSON string and then written to a file named "news_data.json". If the format is "txt", the information is written to a file named "news_data.txt".

* The read_past_text() function takes in a file name and format, reads the file, and prints the contents to the console.

* The convert_time() function prompts the user for a time type (either "minute", "hour", or "second") and a time input. It then converts the time input to seconds and returns the result.

The script also uses a while loop to continuously scrape the website and save the information to the file, with a specified time interval between each scrape, which is convert by convert_time() function. The script also uses the subprocess library to send a system notification after each scrape.
