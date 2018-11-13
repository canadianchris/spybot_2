"""

    spybot_2
    ~~~~~~~~

    SpyBot (Setup PY Bot, get it?!) is a bot built to help Python developers migrate
    their setup.py to setup.cfg

    General features - provide an open github repo, SpyBot will fork, clone and if
    it is able to create a setup.cfg from the files discovered, will submit a PR back to you
    with the setup.cfg

    :license: MIT, I guess?

"""

from github import Github

def parse_response(user_response):
    # clean up the supplied github repo

def read_github_repo(user_github_repo):
    # read the user supplied repo (user_github_repo) first before everything else
    # there's no point forking if there is no setup.py

    g = Github("")

    repo = g.get_repo(user_github_repo)
    contents = repo.get_contents("")

    for content_file in contents:
        if content_file.path == "setup.py":
            print("SUCCESS")
        else:
            print("No setup.py found in this repository")


def fork_github_repo(user_github_repo, spybot_github_repo):
    # fork the user supplied repo (user_github_repo) to spybot's repo

def check_for_spybot_issue(user_github_repo):
    # check the provided repo for a spybot issue - perhaps we should just check for repos that have
    # special "spybot" issue created and go from there?