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

Information about the license under which the repository is released.

## Acknowledgments

- Credit to any other repos, blogs or resources used to create the scripts.
