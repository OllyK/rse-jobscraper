from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

class OxUniJobFinder:

    base_page_url = "https://my.corehr.com/pls/uoxrecruit/erq_search_version_4.start_search_with_params?p_company=10&p_internal_external=E&p_display_in_irish=N&p_competition_type=&p_force_type=E&p_start_from="
    base_job_url ="https://my.corehr.com/pls/uoxrecruit/erq_jobspec_version_4.display_form?p_company=10&p_internal_external=E&p_display_in_irish=N&p_process_type=&p_applicant_no=&p_form_profile_detail=&p_display_apply_ind=Y&p_refresh_search=Y&p_recruitment_id="
    
    def find_jobs(self):
        page_urls = [self.base_page_url + str(x) for x in [0, 100, 200, 300]]
        job_divs = []
        for url in page_urls:
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            mydivs = soup.find_all("td", {"class": "erq_searchv4_result_row"})
            for div in mydivs:
                job_divs.append(div)
        return self.create_output_string(job_divs)

    def create_output_string(self, jobs_list):
        output_string = "Oxford University Jobs\n"
        id_pattern = re.compile(r"(?<!\d)\d{6}(?!\d)")
        job_counter = 0
        for job in jobs_list:
            tds = [x.text.strip().lower() for x in job.find_all("td", class_="erq_searchv4_heading5_text")]
            if "standard grade 8" in tds:
                job_counter += 1
                try:
                    job_title = job.find("td", class_="erq_searchv4_heading4").text.strip()
                    dept = job.find("td", class_="erq_searchv4_heading2").text.strip()
                    vacancy_id = list(filter(id_pattern.match, tds))[0]
                    vacancy_url = self.base_job_url + vacancy_id
                except AttributeError as e:
                    dept = None
                    vacancy_id = list(filter(id_pattern.match, tds))[0]
                    vacancy_url = self.base_job_url + vacancy_id
                output_string += (f"{job_counter}: {job_title}\n")
                output_string += (f"{dept}\n")
                output_string += (f"{vacancy_url}\n\n")
        print(f"{job_counter} Ox Uni jobs found.")
        return output_string

# ox_job = OxUniJobFinder()
# print(ox_job.find_jobs())
