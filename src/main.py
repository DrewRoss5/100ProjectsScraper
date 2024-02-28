import sys
import scraper

# a dictionary associating commands with their paramters and descriptions
COMMAND_DICT = {
    "view": ["", "Displays all project ideas"],
    "view-filtered": ["allowed_categories", "Displays all projects within provided categories see https://github.com/DrewRoss5/100ProjectsScraper/blob/main/README.md for filters"],
    "random": ["project_count OPTIONAL", "Selects a provided number of random projects from all categories. If no count is provided, one random task will be selected"],
    "random-filtered": ["project_count OPTIONAL, allowed_categories", "Selects a provided number of random projects from the provided categories. If no count is provided, one random task will be selected"],

}

# a dicitionary associating shortenings of category names with their 
FILTER_MAP = {
                "web": "General Web & Networking Projects",    
                "bots": "Bots",
                "apps": "Software & Apps",
                "ai": "Artificial Intelligence",
                "cs": "Theoretical Computer Science",
                "crypto": "Cryptography",
                "games": "Simulations, Games and Game AI",
                "misc": "Miscellaneous",
                "challenge": "Coding Challenges"
              }

# parses shortened filters and returns the whole filtered names
def parse_categories(args) -> list[str]:
        # parse allowed categories
        categories = []
        for i in args:
            if i not in FILTER_MAP:
                print(f'Error: Unrecognized category: "{i}"')
                exit(-1)
            else:
                categories.append(FILTER_MAP[i])
        return categories

# prints a list of cammands and their parameters
def print_help():
    print(f'{"Command:".ljust(20)}{"Parameters:".ljust(45)}{"Description:"}\n') 
    for i in COMMAND_DICT:
       project_info = COMMAND_DICT[i]
       print(f'{i.ljust(20)}{project_info[0].ljust(45)}{project_info[1]}') 

# initalize the project list
try:
    projects = scraper.ProjectList()
except ConnectionError as e:
    print(e)
    exit(-1)

# ensure the correct number of argument were provided
args = sys.argv[1:]
if len(args) == 0:
    print('Error - Please provide at least one argument')
    exit(-1)

# determine the user's action and run the appropriate command
command = args[0]
match command:
    case 'random':
        # get the number of random projects the user would like to recieve (default=1)
        if len(args) > 1:
            try:
                project_count = int(args[1])
                if project_count <= 0:
                    raise ValueError()
            except ValueError:
                print('Error - Please provide a valid, positive, non-zero integer.')
                exit(-1)
        else:
            project_count = 1
        # get and display the random projects
        rand_projects = projects.get_random(project_count)
        projects.display(rand_projects)
    
    case 'random-filtered':
        # ensure at least on argument was passed
        if len(args) < 2:
            print("Error - please provide at least one argument")
            exit(-1)
        # determine if a number of projects to get was provided
        if args[1].isdigit() and int(args[1])  >= 1:
            project_count = int(args[1])
            start_index = 2
        else:
            project_count = 1
            start_index = 1
        # filter the possible categories
        categories = parse_categories(args[start_index:])
        projects.filter_categories(categories)
        # get and display the random projects
        rand_projects = projects.get_random(project_count)
        projects.display(rand_projects)


    case 'view-filtered':
        categories = parse_categories(args[1:])
        projects.filter_categories(categories)
        projects.display()
    
    case 'view':
        projects.display()
        
    case 'help':
        print_help()
    
    case _:
        print(f'Unrecognized Command "{command}"\nAvailable Commands:')
        print_help()
        
