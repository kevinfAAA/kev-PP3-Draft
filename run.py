import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find Elements by ID

results = soup.find(id="ResultsContainer")

# Find Elements by HTML Class Name

print(results.prettify())
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end="\n"*2)

# Extract Text From HTML Elements

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# Find Elements by Class Name and Text Content

python_jobs = results.find_all("h2", string="Python")
print(python_jobs)

# Pass a Function to a Beautiful Soup Method (The program will find 10 job
# posts that include the word "python" in their job title!)

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

print(len(python_jobs))
