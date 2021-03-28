from bs4 import BeautifulSoup
import time
from urllib.request import urlopen


class MSDJobFinder:

    base_page_url = "https://jobs.msd.com/gb/en/search-results?keywords=python"
    soup = ""

    def __init__(self, driver):
        self.driver = driver
    
    def find_jobs(self):
        self.job_divs = []
        self.append_job_divs(self.base_page_url)
        pages_parent = self.soup.find("ul", {"class": "pagination"})
        pages = pages_parent.find_all("li", {"class": "au-target"})
        print(f"{len(pages)} pages found on MSD website.")
        
        for index in range(1, len(pages)):
            url_suffix = f"&from={index * 10}&s=1"
            url = self.base_page_url + url_suffix
            self.append_job_divs(url)
        print(f"{len(self.job_divs)} MSD jobs found.")
        return self.create_output_string(self.job_divs)

    def append_job_divs(self, url):
        self.driver.get(url)
        time.sleep(3)
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, "html.parser")
        list_items = self.soup.find_all("li", {"class": "jobs-list-item"})
        for item in list_items:
            self.job_divs.append(item)

    def create_output_string(self, jobs_list):
        output_string = "MSD Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            title_div = job.find("div", class_="job-title")
            job_title = title_div.text.strip()
            vacancy_url = job.find("a", href=True)['href']
            location_div = job.find("div", class_="information")
            location = location_div.find("span", class_="job-location")
            try:
                location = location.text.strip()
            except AttributeError:
                location = "Multiple locations"
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{location}\n")
            output_string += (f"{vacancy_url}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# msd_job = MSDJobFinder(driver)
# print(msd_job.find_jobs())
