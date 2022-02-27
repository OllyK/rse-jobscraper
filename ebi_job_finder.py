from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException

class EbiJobFinder:

    base_page_url = "https://www.embl.org/jobs/ebi/iframe"
    
    def __init__(self, driver):
        self.driver = driver

    def find_jobs(self):
        self.job_divs = []
        self.driver.get(self.base_page_url)
        time.sleep(3)
        self.append_job_divs(self.driver)
        print(f"{len(self.job_divs)} EMBL-EBI jobs found.")
        return self.create_output_string(self.job_divs)

    def append_job_divs(self, driver):
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        list_items = soup.find_all("article", {"class": "vf-summary--job"})
        for item in list_items:
            self.job_divs.append(item)

    def create_output_string(self, jobs_list):
        stem = "https://www.embl.org"
        output_string = "EMBL-EBI Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            url = job.find("a", class_="vf-summary__link", href=True)
            job_title = url.text.strip()
            vacancy_url = url["href"]
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{stem + vacancy_url}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# ebi_job = EbiJobFinder(driver)
# print(ebi_job.find_jobs())
