# BL-useful-script-to-share

This repository contains a collection of useful scripts that are designed to help automate various tasks and make them easier for developers. The scripts cover a wide range of topics such as file manipulation, data processing, and system administration. The purpose of this repository is to share these scripts with the community, in order to help others save time and effort when working on their own projects. These scripts have been tested and are known to work, but feel free to use them as a starting point for your own work and to make any modifications that you see fit.

## Getting Started

Instructions on how to set up and run the scripts will be listed as comments in the scripts.

## Scripts

- github-search.py:

  You can run this code in your local machine with python installed and it will prompt you to enter the search string and it will return the table in a more readable format with 3 columns "name", "html_url", and "forks" and sorted based on the column forks in descending order.

- csv2md.py:

example 1:
   ```
   python csv2md.py file.csv
   ```

This script will process specific conversion of file.csv to file.md

example 2:
  ```
     python csv2md.py
  ```

The script will process all the CSV files in the current folder and create corresponding Markdown files in the same folder.
The original CSV files will remain in the folder.
Note: This script is designed to work with only CSV files in the current folder. Before running the script, make sure that the folder only contains the desired CSV files.

- openAIPhotoGen.py

The code allows the user to input the "prompt" value. The user's input is passed to the API call, which generates an image based on the prompt. The code checks the status code of the response and, if successful, extracts the URL of the generated image and downloads it as a PNG file. If the API call was not successful, an error message is printed with the response code.

Obtain API key at: https://platform.openai.com/account/api-keys 

- check_tcp_established.py:
    
    First, make sure that you have all the required modules installed. The code requires the following modules: os, re, json, urllib, platform, and   prettytable.

    If you encounter a "ModuleNotFoundError" error while running the code, it means that you are missing a required module. To install the missing module, you can use the "pip" command in the command prompt or terminal.

    For example, to install the "prettytable" module, you can run the following command:

    ``` pip install prettytable ```

    If you have installed the missing module, but the error persists, make sure that you are using the correct Python environment. You may need to specify the correct environment or update your PATH variable to point to the correct location.

    If you still encounter an error or are unsure of what to do, you can check the module's documentation or seek help from an expert.

    Finally, if you see a "not found" error while running the code, it means that the code is unable to retrieve information from the API or the netstat command. In this case, you can check your internet connection or verify that the netstat command is installed on your system. If you are unsure of how to install or use the netstat command, you can consult the documentation for your operating system or seek help from an expert.


- ### more to be added

## Built With

- List of technologies or libraries used to create the scripts.

## Contributing

To contribute to this repository, please follow these instructions:

  Fork the repository: Click on the "Fork" button on the top right corner of the repository page on GitHub. This will create a copy of the repository under your own GitHub account.

  Clone the repository: Once you have forked the repository, you can clone it to your local machine. Open a terminal and navigate to the directory where you want to clone the repository. Run the command git clone https://github.com/lambinh/BL-useful-scripts-to-share.git  to clone the repository.

  Create a new branch: Before making any changes, it's a good practice to create a new branch. This will allow you to make changes without affecting the master branch. Run the command git branch [branch_name] to create a new branch.

  Checkout the new branch: Once you have created a new branch, you need to switch to it. Run the command git checkout [branch_name] to switch to the new branch.

  Make changes: You can now make changes to the code. Make sure to test your changes thoroughly before committing them.

  Commit your changes: Once you are satisfied with your changes, you can commit them. Run the command git add . to stage the changes, followed by git commit -m "Commit message" to commit the changes.

  Push your changes: Push your changes to the remote repository by running the command git push origin [branch_name].

  Create a pull request: Once you have pushed your changes, go to the repository page on GitHub and click on the "Compare and pull request" button. Provide a detailed description of your changes and submit the pull request.

Please make sure to follow the project guidelines and coding standards while contributing.

Please also be aware that before merging the pull request, the code will be reviewed by the maintainers, so please be patient and responsive to feedback and suggestions.
## License

GNU GENERAL PUBLIC LICENSE

## Disclaimer and Terms of Use:

Please note that the codes provided on this Github repository is intended for educational purposes only. It is not intended for commercial use or distribution without the express written consent of the owner of the repository. The code is provided as-is and the owner of the repository makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the code. The use of the code is at the user's own risk, and the owner of the repository shall not be liable for any direct, indirect, incidental, special or consequential damages arising out of or in any way connected with the use of the code. By using the code, you acknowledge and agree to these terms and conditions.


## Acknowledgments

- Credit to any other repos, blogs or resources used to create the scripts.
