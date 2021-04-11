from bs4 import BeautifulSoup
import time

class ExscientiaJobFinder:

    base_page_url = "https://www.exscientia.ai/careers"

    def __init__(self, driver):
        self.driver = driver
    
    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.jobs = soup.find_all("li", {"class": "_70bb"})
        print(f"{len(self.jobs)} Exscientia jobs found.")
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "Exscientia Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            vacancy_urls = job.find("a", href=True)
            job_title = job.find("h2", class_="af77").text.strip()
            location = job.find("h6", class_="_957f").text.strip()
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{location}\n")
            output_string += (f"{vacancy_urls['href']}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# exsci_job = ExscientiaJobFinder(driver)
# print(exsci_job.find_jobs())
