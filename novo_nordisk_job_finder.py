from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException

class NovoNordiskJobFinder:

    base_page_url = "https://www.novonordisk.com/careers/find-a-job/career-search-results.html?searchText=python&countries=Denmark;United%20States;China%20Mainland;Argentina;Australia;Belgium;Brazil;Canada;Chile;Colombia;Egypt;Finland;France;Germany;India;Indonesia;Iraq;Israel;Italy;Japan;Kazakhstan;Kuwait;Malaysia;Mexico;Netherlands;Oman;Pakistan;Poland;Qatar;Russia;Saudi%20Arabia;Serbia;Slovakia;Slovenia;South%20Korea;Spain;Switzerland;Taiwan;Thailand;Tunisia;Turkey;Ukraine;United%20Arab%20Emirates;United%20Kingdom;Vietnam&categories=Clinical%20Development%20and%20Medical;Communication%20and%20Corporate%20Affairs;Engineering;General%20Management%20and%20Administration;Human%20Resource%20Management;Information%20Technology%20&%20Telecom;Manufacturing;Marketing%20and%20Market%20Access;Quality;Regulatory;Research;Supply%20Chain%20and%20Procurement;Finance;Legal,%20Compliance%20and%20Audit;Sales"
    
    def __init__(self, driver):
        self.driver = driver

    def find_jobs(self):
        self.driver.get(self.base_page_url)
        time.sleep(3)
        #Accept Cookies
        link = self.driver.find_element_by_xpath(".//button[@class='ot-pc-refuse-all-handler']")
        self.driver.execute_script("arguments[0].click();", link)
        time.sleep(1)
        # Click on the more jobs link
        more_jobs = True
        while more_jobs:
            try:
                link = self.driver.find_element_by_xpath(".//div[@class='button-wrapper']")
                self.driver.execute_script("arguments[0].click();", link)
                time.sleep(2)
            except NoSuchElementException:
                more_jobs = False
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # Click on every job advert in order to get the link URL and append to another list
        listing_links = self.driver.find_elements_by_xpath(".//div[contains(@class, 'element-box')]")
        self.listing_links = []
        main_window = self.driver.current_window_handle
        for listing in listing_links:
            listing.click()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.listing_links.append(self.driver.current_url)
            self.driver.close()
            self.driver.switch_to.window(main_window)
        self.jobs = soup.find_all("div", {"class": "element-box"})
        print(f"{len(self.jobs)} NovoNordisk jobs found.")
        return self.create_output_string(self.jobs)

    def create_output_string(self, jobs_list):
        output_string = "NovoNordisk Jobs\n"
        for count, job in enumerate(jobs_list, start=1):
            job_title = job.find("div", class_="title-desktop").text.strip()
            job_location = job.find("div", class_="flex-basis-l-4").text.strip()
            output_string += (f"{count}: {job_title}\n")
            output_string += (f"{job_location}\n")
            output_string += (f"{self.listing_links[count - 1]}\n\n")
        return output_string

# from utils import get_webdriver
# driver = get_webdriver()
# nn_job = NovoNordiskJobFinder()
# print(nn_job.find_jobs())
