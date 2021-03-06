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
- Society of Research Software Engineering website - All jobs
- Exscientia - All jobs
- Novartis - Jobs with the tag "python" in the following countries: AU,AT,BB,BE,BA,BR,CA,HR,CZ,DK,EE,FI,FR,GE,DE,GR,HU,IE,IT,LV,LT,LU,MK,MD,NZ,NO,PL,PT,RS,SG,SK,SI,ES,SE,CH,GB.
- EMBL-EBI - All jobs

### Requirements
A python environment with:
- BeautifulSoup
- Selenium

You will also need to download and install the [Chrome Webdriver](https://chromedriver.chromium.org/downloads) to use with Selenium.  Once downloaded, change the path in `utils.py`.

### Useage
If you want to send an email enter your from/to address and password in the appropriate place in jobscraper.py.

To run the script:
```shell
python jobscraper.py
```
