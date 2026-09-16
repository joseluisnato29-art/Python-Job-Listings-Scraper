try:
    import csv
    import requests
    from requests.exceptions import ConnectionError, Timeout, HTTPError
    from bs4 import BeautifulSoup
except ImportError as e:
    missing_library=e.name
    print(f"The {missing_library} couldn't be imported. Please install the requiered dependencies")
    exit(1)
# Web page URL
url="https://realpython.github.io/fake-jobs/"
# Prevents a NameError if there's an error
response=None
try:
    # HTTP request with timeout, prevents scrapper to keep hanging
    response=requests.get(url, timeout=10)
except ConnectionError as ce:
    print(f"Conection Error (DNS, network outage, IP blocking): {ce}")
except Timeout as te:
    print(f"The request exhaust time limit: {te}")
except HTTPError as he:
    print(f"HTTP error returned by server: {he}")
except Exception as e:
    print(f"Unexpected error when trying to connect: {e}")

# Function to detecct missing fields, if one field returns None, the cell is filled with N/A otherwise is converted to text.
def safe_extract(job,tag,class_name):
    element=job.find(tag,class_=class_name)
    return element.text.strip() if element else "N/A"
# The code below is executed only if web request was successful (response.status_code==200)
if response and response.status_code==200:
    # bs4 process the page content
    soup=BeautifulSoup(response.text,'html.parser')
    # The job info we were asked to extract are: title, company name, location, link for details. All of them are contained in
    # <div class="card-content">, there's one card-content for each job, so we extract the info of every one of them.
    jobs=soup.find_all('div', class_='card-content')
    # Write in each column of 'jobs.csv', newline='' prevents duplicated line breaks.
    with open('jobs.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        # Define column names
        columns=['id','job_title','company_name','location','details_url']
        # Creates an object that allows write data using dictionaries, keys match the list of columns
        writer=csv.DictWriter(csv_file, fieldnames=columns)
        # Iterate for each car-content to extract the searched data
        for i, job in enumerate(jobs,1):
            title=safe_extract(job,'h2','title')
            c_name=safe_extract(job,'h3','subtitle')
            locat=safe_extract(job,'p','location')
            link_tag=job.find('a',string='Apply')
            link=link_tag['href'] if link_tag else "N/A"
            # Write the data into the CSV file
            writer.writerow({
                'id':i,
                'job_title':title,
                'company_name':c_name,
                'location':locat,
                'details_url':link
            })
        print(f"Data exported successfully!, {i} registers extracted.")
else: print(f"Failed to scrape {url}.")
