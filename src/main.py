import sys
import scraper

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
    
    case 'view-filtered':
        # parse allowed categories
        categories = []
        for i in args[1:]:
            if i not in FILTER_MAP:
                print(f'Error: Unrecognized category: "{i}"')
                exit(-1)
            else:
                categories.append(FILTER_MAP[i])
        projects.filter_categories(categories)
        projects.display()
    
    case 'view':
        projects.display()
        
    case _:
        print(f'Error - "{command}" is not a recognized command.')