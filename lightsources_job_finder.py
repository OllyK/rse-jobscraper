from bs4 import BeautifulSoup
import time

class LightsourceJobFinder:

    base_page_url = "https://lightsources.org/careers/"

    def __init__(self, driver):
        self.driver = driver
    
    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        # Click on the more jobs link
        for _ in range(5):
            link = self.driver.find_element_by_xpath(".//a[@class='load_more_jobs']")
            self.driver.execute_script("arguments[0].click();", link)
            time.sleep(2)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.jobs = soup.find_all("li", {"class": "job_listing"})
        print(f"{len(self.jobs)} lightsources.org jobs found.")
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "lightsources.org Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            vacancy_url = job.find("a", href=True)
            job_info = vacancy_url.find("div", class_="position")
            job_title = job_info.text.strip()
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{vacancy_url['href']}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# ls_job = LightsourceJobFinder(driver)
# print(ls_job.find_jobs())
