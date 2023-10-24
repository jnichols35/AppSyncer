import requests
import json
from bs4 import BeautifulSoup

url = "https://docs.delinea.com/online-help/privilege-manager/install/sw-downloads.htm#AgentSoftware"
file_path = "JSON/thycotic.json"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
version_elements = soup.select('.TableStyle-Alternate-Row-Color-BodyE-Column1-Body2, .TableStyle-Alternate-Row-Color-BodyE-Column1-Body1')
uri_elements = soup.select('.TableStyle-Alternate-Row-Color-BodyD-Column1-Body2, .TableStyle-Alternate-Row-Color-BodyD-Column1-Body1')
data_list = []

for version, uri_parent in zip(version_elements, uri_elements):
    version_number = version.get_text(strip=True)
    uri_child = uri_parent.find('a')
    if uri_child:
        uri_value = uri_child['href']
        product_name = uri_child.get_text(strip=True)
        data = {
            "product_name": product_name,
            "version_number": version_number,
            "URI": uri_value
        }
        data_list.append(data)


with open(file_path, 'w') as json_file:
    json.dump(data_list, json_file, indent=1)
