from bs4 import BeautifulSoup
import time

class RosalindJobFinder:

    base_page_url = "https://opportunities.rfi.ac.uk/vacancies.html"

    def __init__(self, driver):
        self.driver = driver
        
    def find_jobs(self):
        job_divs = []
        self.driver.get(self.base_page_url)
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.jobs = soup.find_all("div", {"class": "jobCard"})
        print(f"{len(self.jobs)} Rosalind Franklin jobs found.")
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "Rosalind Frankin Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            job_info = job.find("h2", class_="card-title")
            job_title = job_info.text.strip()
            vacancy_url = job_info.find("a", href=True)['href']
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{vacancy_url}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# ros_job = RosalindJobFinder(driver)
# print(ros_job.find_jobs())
