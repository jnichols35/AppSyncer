import requests
import json

from bs4 import BeautifulSoup

pkg_id = "Perimeter81Ltd.Perimeter81Ltd"
file_path = "JSON/perimeter81.json"

url = "https://support.perimeter81.com/docs/downloading-the-agent"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

msi_link = soup.find("a", href=lambda href: href and href.endswith(".msi"))
if msi_link:
    msi_url = 'http:' + msi_link["href"]
    version_number = msi_url.split("_")[-1].split(".msi")[0]
    data = {
        "package_id": pkg_id,
        "version_number": version_number,
        "msi_url": msi_url
    }

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=1)
else:
    print("MSI link not found on the webpage.")
