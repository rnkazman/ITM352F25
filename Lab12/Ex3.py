# Parse the UH Shilder ITM department page and extract names of faculty members
import ssl
import urllib.request
from bs4 import BeautifulSoup

itm_url = " https://shidler.hawaii.edu/itm/people"
ssl._create_default_https_context = ssl._create_unverified_context

itm_html = urllib.request.urlopen(itm_url)
html_to_parse = BeautifulSoup(itm_html, "html.parser")
#print(html_to_parse)    # Inspect the HTML to find the tags that contain the information we want

pretty_html = html_to_parse.prettify()
lines = pretty_html.splitlines()
num_to_print = 10
print("Pretty printing the first " + str(num_to_print) + " lines of the HTML:")

# Print the first few lines of the prettified HTML
for line in lines[:num_to_print]:
    print(line)

# Find and print just the names of faculty members
list_of_ITM_faculty = html_to_parse.find_all("h2", class_="title")

# Create a list with just the names
itm_faculty = []
for element in list_of_ITM_faculty:
    itm_faculty.append(element.text)
    print(element.text)

print("Number in the initial list:", len(list_of_ITM_faculty))
unique_itm_faculty = list(set(itm_faculty))
print("Number of unique faculty names:", len(unique_itm_faculty))
