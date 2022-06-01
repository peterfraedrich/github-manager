from github import Github # requires pip install pygithub
from datetime import datetime, timedelta
import os, re

# Searches for open pull requests by team, older than today
def get_team_open_pull_requests():
  # Establish session
  g = Github(session)
  try:
    team_name = os.environ['TEAMNAME']
    for issue in g.search_issues(f'org:IDme is:pr is:open draft:false team-review-requested:IDme/{team_name}'):
      now = datetime.now()
      now_date = now.date()
      created_date = issue.created_at.date()
      if created_date > now_date:
        print(issue.title)
        print('Opened by ' + issue.user.login + ' * ' + issue.html_url)
  except:
    pass

get_team_open_pull_requests(session)
