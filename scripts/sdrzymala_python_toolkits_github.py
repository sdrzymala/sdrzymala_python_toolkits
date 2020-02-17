import requests
import json
import subprocess
import os
import argparse

# user variables
parser = argparse.ArgumentParser(description='python toolkit github - clone all repositories from github saccount')
parser.add_argument('--github_account_name', type=str, help='github account name', default='sdrzymala')
parser.add_argument('--local_repositoey_directory', type=str, help='local repository directory', default=r'/home/sdrzymala/code/github')
args = parser.parse_args()
github_account_name = args.github_account_name
local_repository_directory = args.local_repositoey_directory

# scipt variables
github_api_url = "https://api.github.com/users/" + github_account_name + "/repos"

# get all repositories for user from github
request = requests.get(github_api_url)
repositories = json.loads(request.content)
repositories_names = [x["name"] for x in repositories]

# clone repository if doesn't exist or pull if exists
for repository_name in repositories_names:
    current_repository_url = "https://github.com/{}/{}.git".format(github_account_name, repository_name)
    current_repository_directory = "{}/{}".format(local_repository_directory, repository_name)

    if not os.path.exists(current_repository_directory):
        print ("cloning repository {}".format(repository_name))
        os.chdir(local_repository_directory)
        subprocess.check_call(['git', 'clone', current_repository_url])
    else:
        print ("repository {} already cloned".format(repository_name))