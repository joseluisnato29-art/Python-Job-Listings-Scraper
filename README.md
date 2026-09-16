# Python-Job-Listings-Scraper
## Description
This is a begginer's project taken from the Data Analyst roadmap in Roadmap.sh<br>
Project URL: https://roadmap.sh/projects/job-listings-scraper
The scrapper extracts the next information from a Fake Job Website: job title, company name, location and the link to the full job description.
The fake site was made intentionally for learning the basic concepts and tools used on scrapping, this allowed me to understand the HTML structure, select elements without problems, and to process data without having to deal with anti-scraping protections or legal restrictions.
## Background
<b>Scraper:</b> program or bot designed to extract info automatically.<br>
<b>Web Scraper:</b> program that simulates human web navigation: starts analyzing HTML code and the web structure, then sends HTTP requests to the web server to recolect data (prices, texts, catalogs) which is saved on DB, or excel and CSV files.<br>
It is mainly used to get: real time e-shop price product tracking and comparison, review and analize collections, data, trends or large volumes of public content to train LLMs (AI).<br>
Extract public data without copyright is legal, but override servers with requests isn't.<br>
A scraper works as follows:
<ol>
<li>Select the web page URL.</li>
<li>Inspect the HTML page code with developer tools by pressing F12 or right click and then Inspect. Locate the specific data requiered.</li>
<li>Send the HTTP request via code to get the web page content.</li>
<li>Parsing: the library process the code obtained and analizes the page structure.</li>
<li>The library extracts the data (texts, images or links) through css selectors, xpath routes and regex.</li>
<li>The library cleans, organizes and exports the obtained info as CSV or DB format.</li>
</ol>
<b>Libraries:</b>
<ul>
<li><b>requests:</b> fetch data from the web, sends HTTP requests to a server and downloads the raw HTML content of a webpage.</li>
<li><b>beautifulsoup:</b> parses and extracts data, cleans up raw HTML and allows to search, filter and navigate tags to extract specific text, links or images.</li>
<li><b>csv:</b> stores and organizes data, writes the extracted structured data into a CSV file.</li>
</ul>
