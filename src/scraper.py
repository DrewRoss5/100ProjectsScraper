import random
import requests
from bs4 import BeautifulSoup


class ProjectList:
    # gets all of the projects on the list
    def __init__(self) -> None:
        req = requests.get("https://github.com/arpit-omprakash/100ProjectsOfCode/blob/main/README.md")
        if (req.status_code != 200):
            raise ConnectionError("Cannot retrieve the task list")
        soup = BeautifulSoup(req.content, 'html.parser')
        # create a list of categories (the first three h3's in the file)
        self.projects = {}
        self.categories = []
        for i in soup.find_all('h3')[:9]:
            self.categories.append(i.text)
            self.projects[i.text] = []
        lists = soup.select('[class*="contains-task-list"]')
        for i in range(len(lists)):
            for project in lists[i].findChildren('a'):
                self.projects[self.categories[i]].append(project.text)

    # prints all projects in a dictionary with indented formatting, if no dictionary is provided, this will default to all projecs
    def display(self, project_dict: dict[str, str] = None):
        if not project_dict:
            project_dict = self.projects
        for i in project_dict:
            print(f'{i}:')
            for project in project_dict[i]:
                print(f'\t{project}')

    # get n random projects from the dictionary, projects are returned as a dictionary using project categories as keys
    def get_random(self, n: int) -> dict[str, str]:
        project_dict = {}
        for i in range(n):
            category = random.choice(self.categories)
            project = random.choice(self.projects[category])
            if category in project_dict:
                project_dict[category].append(project)
                self.delete_project(project, category)
            else:
                project_dict[category] = [project]
                self.delete_project(project, category)
        return project_dict

    # removes a project from the dictionary, and deletes the category if it's empty
    def delete_project(self, project: str, category: str) -> None:
        self.projects[category].remove(project)
        if len(self.projects[category]) == 0:
            del self.projects[category]
            self.categories.remove(category)
        
    # removes all categories other than the ones specified
    def filter_categories(self, new_categories: list[str]):
        for i in self.categories:
            if i not in new_categories:
                del self.projects[i]
        self.categories = new_categories
