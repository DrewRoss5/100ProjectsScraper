# 100ProjectsScraper
A webscraper for <a href="https://github.com/arpit-omprakash/100ProjectsOfCode" target="_blank">100ProjectsOfCode</a>, used to get random programming projects

# Roadmap:
<ul>
  <li>Create documentation</li>
  <li>Allow filtering random projects by category</li>
  <li>Add a "help" command</li>
  <li>Add project descriptions</li>
</ul>

## Installation:
There is no official installer, so the current preferred method is to simply run the python script directly by using `python src/main.py` from this repo's directory. Please ensure that you have Beautiful Soup 4 installed by running `pip install beautifulsoup4`

## Usage:
Once the program is run, it automatically retrieves the data from 100ProjectsOfCode, there are currently three options:<br>
### view:
This command takes no arguments and displays all of the projects organized by category
### view-filtered \[categories]:
This command displays only projects of certain provided categories. The categories use shortened versions of their names in the official markdown document. The category names and their respective category in the markdown document are as follows:
<ul>
  <li>"web" for "General Web & Networking Projects"</li>
  <li>"bots" for "Bots"</li>
  <li>"apps" for "Software & Apps"</li>
  <li>"ai" for "Artifical Intelligence"</li>
  <li>"cs" for "Theoretical Computer Science"</li>
  <li>"games" for "Simulations, Games and Game AI"</li>
  <li>"misc" for "Miscellaneous"</li>
  <li>"challenge" for "Coding Challenges"</li>
</ul>

### random \[project_count]:
Displays `project_count` random projects from any category. If no project_count is provided, one random project will be generated.

### random-filtered \[project_count OPTIONAL] \[categories]:
Displays `project_count` random projects from provided categories. Providing a project count is optional, if no project count is provided, one random project will be selected. Categories follow the formatting of `view-filtered`
