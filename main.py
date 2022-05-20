#!/usr/bin/env python3

import sys
import actions
import argparse

ARGS: argparse.Namespace


def parse_args() -> None:
    global ARGS
    argument_parser = argparse.ArgumentParser(prog="github-manager", description="Manages some shit in GitHub")
    argument_parser.add_argument("--token", "-t", help="GitHub Personal Access Token (PAT) to use for auth")
    argument_parser.add_argument("--action", "-a", help="What action to take")
    argument_parser.add_argument("--org", "-o", help="The GitHub org to target for operations")
    argument_parser.add_argument("--team", "-T", help="Team name to target for operation")
    argument_parser.add_argument("--access", "-A", help="Access level to give (admin, maintain, pull, push, triage)")
    argument_parser.add_argument("--force", "-f", help="Force changes", action="store_true")
    ARGS = argument_parser.parse_args()
    return


def main():
    global ARGS
    if not ARGS.action:
        print("You must supply an --action !")
        sys.exit(1)
    try:
        session = actions._session(pat=ARGS.token)
        fn = getattr(actions, ARGS.action)
        fn(g=session, args=ARGS)
    except Exception as e:
        print(e)
    return


if __name__ == "__main__":
    parse_args()
    print(ARGS)
    main()
