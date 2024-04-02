import requests
import json
from bs4 import BeautifulSoup


class NoQuoteEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def default(self, obj):
        if obj == "URI":
            return obj
        return super().default(obj)


url = "https://docs.delinea.com/online-help/privilege-manager/install/sw-downloads.htm#AgentSoftware"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
version_elements = soup.select('.TableStyle-Alternate-Row-Color-BodyE-Column1-Body2, .TableStyle-Alternate-Row-Color-BodyE-Column1-Body1')
uri_elements = soup.select('.TableStyle-Alternate-Row-Color-BodyD-Column1-Body2, .TableStyle-Alternate-Row-Color-BodyD-Column1-Body1')


product_names = {
    "Core Thycotic Agent (x64)": "DelineaInc.ThycoticAgent",
    "Application Control Agent (x64)": "DelineaInc.ThycoticApplicationControlAgent",
    "Local Security Solution Agent (x64)": "DelineaInc.ThycoticLocalSecurityAgent"
}

data_list = []

for version, uri_parent in zip(version_elements, uri_elements):
    version_number = version.get_text(strip=True)
    uri_child = uri_parent.find('a')
    if uri_child:
        uri_value = uri_child['href']
        product_name = uri_child.get_text(strip=True)
        if product_name in product_names:
            base_product_name = product_name.split('(')[0].strip()
            modified_product_name = product_names[product_name]
            uri = uri_value
            modified_uri = uri.replace("_x64", "_x86")
            data = {
                "product_name": modified_product_name,
                "version_number": version_number,
                "URI": uri + " " + modified_uri
            }
            data_list.append(data)


for data in data_list:
    modified_product_name = data["product_name"]
    filename = f"JSON/{modified_product_name}.json"

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=1, cls=NoQuoteEncoder)

    print(f"JSON file '{filename}' has been created successfully.")
