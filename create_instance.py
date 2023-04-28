#!/usr/bin/env python
from github import Github
g = Github("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")

for repo in g.get_user().get_repos():
    print(repo)