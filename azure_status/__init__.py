import re
import requests
from bs4 import BeautifulSoup

class AzureStatus:
    url = 'https://azure.microsoft.com/en-gb/status/'

    @staticmethod
    def _parse_content(content):
        def __clean_text(text):
            return re.sub("[^a-z0-9\ \.]*","", text).strip().replace(" ","_")

        soup = BeautifulSoup(content, 'html.parser')
        update_time = soup.find_all(class_='updated-time')[0].get_text()
        data_tables = soup.find_all(class_='region-status-table')

        statuses = {}
        for data_table in data_tables:
            zone_name = __clean_text(data_table.get('data-zone-name').strip().lower())
            statuses[zone_name] = {}

            head = data_table.find_all(class_='status-table-head')
            data = data_table.find('tbody')

            headers = [__clean_text(x.get_text().strip().lower()) for x in head[0].find_all('th')]
            data_trs = data.find_all('tr')

            data = {}
            title = None
            for html_tr in data_trs:
                html_cl = html_tr.get('class')
                if html_cl and html_cl[0] == 'status-category':
                    category = __clean_text(html_tr.get_text().strip().lower())
                    data = {}
                else:
                    i = 0
                    for html_td in html_tr.find_all('td'):
                        if i == 0:
                            title = __clean_text(html_td.get_text().strip().lower())
                            data[title] = {}
                        else:
                            stat = html_td.find(class_='hide-text').get_text().strip().lower()
                            if stat != 'blank':
                                data[title][headers[i]] = stat
                        i += 1
                try:
                    statuses[zone_name][category] = data
                except:
                    pass

        return [update_time, statuses]

    def status(self):
        response = requests.get(self.url)
        return self._parse_content(response.text)
