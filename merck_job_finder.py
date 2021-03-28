from bs4 import BeautifulSoup
import time

class MerckJobFinder:

    base_page_url = "https://www.merckgroup.com/en/careers/job-search.html?query%3Apython%2Cpage%3A0%2Ccountry%3Aall%2Cstate%3Aall%2Ccity%3Aall%2CfunctionalArea%3Aall%2CcareerLevel%3Aall%2CemploymentType%3Aall"
    
    def __init__(self, driver):
        self.driver = driver

    def find_jobs(self):
        self.job_divs = []
        self.driver.get(self.base_page_url)
        time.sleep(5)
        self.append_job_divs(self.driver)
        pages = self.driver.find_element_by_xpath("//ol[@class='se-pagination-list']")
        jobs_pages = pages.find_elements_by_xpath(".//li[contains(@class, 'se-pagination-list-item')]")
        print(f"{len(jobs_pages)} pages found on Merck website.")
        for index in range(1, len(jobs_pages)):
            div = jobs_pages[index].find_element_by_xpath(".//div[@role='link']")    
            self.driver.execute_script("arguments[0].click();", div)
            time.sleep(5)
            result = self.driver.find_elements_by_xpath(".//li[@class='se-list-job-item']")
            self.append_job_divs(self.driver)
            pages = self.driver.find_element_by_xpath("//ol[@class='se-pagination-list']")
            jobs_pages = pages.find_elements_by_xpath(".//li[contains(@class, 'se-pagination-list-item')]")
        print(f"{len(self.job_divs)} Merck jobs found.")
        return self.create_output_string(self.job_divs)

    def append_job_divs(self, driver):
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        list_items = soup.find_all("li", {"class": "se-list-job-item"})
        for item in list_items:
            self.job_divs.append(item)

    def create_output_string(self, jobs_list):
        output_string = "Merck Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            title_div = job.find("div", class_="se-list-job-item-title")
            job_title = title_div.text.strip()
            vacancy_url = title_div.find("a", href=True)['href']
            location = job.find("p", class_="se-list-job-item-location").text.strip()
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{vacancy_url}\n")
            output_string += (f"{location}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# merck_job = MerckJobFinder(driver)
# print(merck_job.find_jobs())
