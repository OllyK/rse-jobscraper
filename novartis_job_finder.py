from bs4 import BeautifulSoup
import time

class NovartisJobFinder:

    base_page_url = "https://www.novartis.co.uk/careers/career-search#country=AU,AT,BB,BE,BA,BR,CA,HR,CZ,DK,EE,FI,FR,GE,DE,GR,HU,IE,IT,LV,LT,LU,MK,MD,NZ,NO,PL,PT,RS,SG,SK,SI,ES,SE,CH,GB&keyword=python"

    def __init__(self, driver):
        self.driver = driver
    
    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        self.jobs = soup.find_all("div", {"class": "res-wrapper"})
        print(f"{len(self.jobs)} Novartis jobs found.")
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "Novartis Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            vacancy_url = job.find("a", href=True)
            location = job.find("div", class_="location").text.strip()
            job_title = vacancy_url.text.strip()
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{location}\n")
            output_string += (f"{vacancy_url['href']}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# novartis_job = NovartisJobFinder(driver)
# print(novartis_job.find_jobs())
