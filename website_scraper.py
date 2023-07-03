import requests
from bs4 import BeautifulSoup

# URL of the web page to extract HTML and CSS from
url = input('url:')
# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all <style> tags and extract their content
css_code = ""
for style_tag in soup.find_all("style"):
    css_code += style_tag.string.strip()

# Extract the HTML code
html_code = soup.prettify()

# Save HTML to a file
with open("example.html", "w") as html_file:
    html_file.write(html_code)

# Save CSS to a file
with open("example.css", "w") as css_file:
    css_file.write(css_code)

print("HTML and CSS code saved to files.")
