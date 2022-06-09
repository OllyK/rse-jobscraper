from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException

class ExeterJobFinder:

    base_page_url = "https://jobs.exeter.ac.uk"
    search_term = "software"
    job_url_root = "https://jobs.exeter.ac.uk/hrpr_webrecruitment/wrd/run/"
    
    def __init__(self, driver):
        self.driver = driver

    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        #Put search term into text box
        text_box = self.driver.find_element_by_xpath(".//input[@id='title']")
        text_box.send_keys(self.search_term)
        #Select 30 results per page
        self.driver.find_element_by_xpath(".//select[@id='results']/option[text()='30']").click()
        button = self.driver.find_element_by_xpath(".//input[@id='BU_SEARCH.FRM_BUTTON.ET_BASE.1-1']")
        # Click the Search button
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.jobs = soup.find_all("table", {"class": "sect_header res_sect_header"})
        print(f"{len(self.jobs)} University of Exeter jobs found.")
        # return self.jobs
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "University of Exeter Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            job_title = job.find("a", class_="job-result-title").text.strip()
            job_url = self.job_url_root + job.find("a", class_="job-result-title", href=True)['href']
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{job_url}\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# ext_job = ExeterJobFinder(driver)
# print(ext_job.find_jobs())
# driver.quit()
