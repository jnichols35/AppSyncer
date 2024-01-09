# AppSyncer
AppSyncer is a Python-based tool that automates the process of syncing specific applications with Winget when they are updated. Winget is a package manager for Windows that allows easy installation and management of applications from the command line or script.

## Features
- Automatically detects application updates.
- Syncs updated applications with Winget for easy installation and management.
- Provides a streamlined workflow for keeping applications up-to-date.

## Installation
- Ensure you have Python installed on your system (Python Installation Guide).
- Clone this repository to your local machine using the following command:
```shell
git clone https://github.com/jnichols35/AppSyncer.git
```

Change to the repository's directory:
```shell
cd AppSyncer
```

Install the required dependencies:
```shell
    pip install -r requirements.txt
  ```
## Usage
A python script should be created to locate and generate a json file for the latest version of a software. It should be saved in the `apps` folder.

Example of what the json file should look like. 
```json
{
 "package_id": "CompanyID.AppName",
 "version_number": "1.0.0",
 "msi_url": "https://localhost/windows_app(x86).msi,https://localhost/windows_app(x64).msi"
}
```
- Replace `"CompanyID.AppName"` with the existing package id, or create a new one.
- Replace `"1.0.0"` with the current version of the application.
- Replace `"https://localhost/windows_app.msi"` with the url(s) used to install the current version of the application. 

Run the appsyncer.py script:
```shell
    python appsyncer.py
```

The script will check for updates to the specified applications based on the scripts in the `apps` and sync them with Winget.

## Contributing
Contributions to AppSyncer are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the repository.

If you would like to contribute code changes, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear descriptions.
4. Push your changes to your forked repository.
5. Submit a pull request, explaining the changes you have made.

## License
This project is licensed under the MIT License.

## Acknowledgements
AppSyncer is built upon the following open-source libraries:
- [Python](https://www.python.org/)
- [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [Komac](https://github.com/russellbanks/Komac)
