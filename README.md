# rse-jobscraper
A python program to scrape some websites for pharma/synchrotron research software engineering jobs. The program will save the results out to a text file and also send an email. To send an email using a Gmail account, you'll need to have allowed access to less secure apps in the security settings. 

### Sites
At present, sites scraped are:
- Oxford University - All grade 8 jobs
- lightsources.org - The last 60 jobs posted
- The Rosalind Franklin Institute - All jobs
- Merck - All jobs that contain the tag "python"
- MSD - All jobs that contain the tag "python"
- NovoNordisk - All jobs that contain the tag "python"

### Requirements
A python environment with:
- BeautifulSoup
- Selenium

### Useage
If you want to send an email enter your from/to address and password in the appropriate place in jobscraper.py.

To run the script:
```shell
python jobscraper.py
```
