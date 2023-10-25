import os
import subprocess

json_path = "JSON"
if not os.path.exists(json_path):
    os.makedirs(json_path)

folder_path = 'apps'
file_list = os.listdir(folder_path)
python_scripts = [file for file in file_list if file.endswith('.py')]

for script in python_scripts:
    script_path = os.path.join(folder_path, script)
    subprocess.run(['python', script_path])