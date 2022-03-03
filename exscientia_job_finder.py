from bs4 import BeautifulSoup
import time
import json

class ExscientiaJobFinder:

    base_page_url = "https://www.exscientia.ai/careers"

    def __init__(self, driver):
        self.driver = driver
    
    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.driver.quit()
        json_out = soup.find('script', id="__NEXT_DATA__")
        script = json_out.contents[0].string
        data = json.loads(script)
        jobs = data['props']['pageProps']['allJobs']
        print(f"{len(jobs)} Exscientia jobs found.")
        return self.create_output_string(jobs)

    def create_output_string(self, jobs_list):
        output_string = "Exscientia Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            vacancy_urls = job['shortlink']
            job_title = job['full_title']
            location = job['location']['location_str']
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{location}\n")
            output_string += (f"{vacancy_urls}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# exsci_job = ExscientiaJobFinder(driver)
# print(exsci_job.find_jobs())
# driver.quit()
