from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException

class EbiJobFinder:

    base_page_url = "https://www.ebi.ac.uk/about/jobs"
    
    def __init__(self, driver):
        self.driver = driver

    def find_jobs(self):
        self.job_divs = []
        self.driver.get(self.base_page_url)
        time.sleep(3)
        self.append_job_divs(self.driver)
        # Click on the more jobs link
        more_jobs = True
        while more_jobs:
            try:
                link_wrapper = self.driver.find_element_by_xpath(".//li[contains(@class, 'pager-next')]")
                link = link_wrapper.find_element_by_xpath(".//a")
                self.driver.get(link.get_attribute("href"))
                time.sleep(2)
                self.append_job_divs(self.driver)
            except NoSuchElementException as e:
                more_jobs = False
        print(f"{len(self.job_divs)} EMBL-EBI jobs found.")
        return self.create_output_string(self.job_divs)

    def append_job_divs(self, driver):
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        list_items = soup.find_all("div", {"class": "job-item-row"})
        for item in list_items:
            self.job_divs.append(item)

    def create_output_string(self, jobs_list):
        output_string = "EMBL-EBI Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            title_div = job.find("div", class_="views-field-nothing-1")
            job_title = title_div.text.strip()
            vacancy_url = title_div.find("a", href=True)['href']
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{vacancy_url}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# ebi_job = EbiJobFinder(driver)
# print(ebi_job.find_jobs())
