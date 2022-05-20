import argparse
import github


def _session(pat: str) -> github.Github:
    """
    starts a GitHub session with the provided PAT
    param: pat -- Personal Access Token
    """
    return github.Github(pat)


def _set_org(g: github.Github, org: str) -> github.Organization:
    """
    sets the current organization to use
    param: g -- github session
    param: org -- org name
    """
    return g.get_organization(login=org)


def give_access(g: github.Github, args: argparse.Namespace) -> None:
    """
    gives access to all repos in an org to a team
    param: args.org -- org name
    param: args.team -- team name
    param: args.access -- access level to give (admin, maintain, pull, push, triage)
    param: args.force -- force changes to existing access
    """
    org = _set_org(g, args.org)
    teams = org.get_teams()
    repos = org.get_repos()
    for t in teams:
        if t.name == args.team:
            for r in repos:
                perms = t.get_repo_permission(r)
                if perms is None or args.force:
                    print(f"Setting {r.name} to {args.access}")
                    t.set_repo_permission(r, args.access)
                else:
                    print(f"Skipping {r.name}")

    return
