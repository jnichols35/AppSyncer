import json

filename = "JSON/perimeter81.json"
with open(filename, 'r') as json_file:
    data = json.load(json_file)

package_id = data["package_id"]
version_number = data["version_number"]
urls = data["msi_url"]
string = f"update --id {package_id} --version {version_number} --urls {urls} --submit"
print(string)