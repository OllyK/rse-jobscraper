from bs4 import BeautifulSoup
import time

class SocRSEJobFinder:

    base_page_url = "https://society-rse.org/careers/vacancies/"

    def __init__(self, driver):
        self.driver = driver
    
    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.jobs = soup.find_all("li", {"class": "job_listing"})
        print(f"{len(self.jobs)} Society of RSE jobs found.")
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "Society of RSE Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            vacancy_url = job.find("a", href=True)
            job_title = vacancy_url.find("div", class_="position").text.strip()
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{vacancy_url['href']}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# s_rse_job = SocRSEJobFinder(driver)
# print(s_rse_job.find_jobs())
