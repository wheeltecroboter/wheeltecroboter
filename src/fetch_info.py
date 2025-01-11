import os
from dotenv import load_dotenv
from github import Github
from collections import Counter

def get_lines_of_code(g: Github) -> int:
    total_lines = 0

    for repo in g.get_user().get_repos():
        try:
            languages = repo.get_languages()
            total_lines += sum(languages.values())
        except Exception:
            return 0
        return total_lines

def get_languages(g: Github) -> dict:
    languages = Counter()

    for repo in g.get_user().get_repos():
        try:
            for lang, bytes_count in repo.get_languages().items():
                languages[lang] += bytes_count
        except Exception:
            continue
        return dict(languages)


def fetch_stats(g:Github) -> dict:
    user = g.get_user()
    return {
        "username": user.login,
        "followers": user.followers,
        "following": user.following,
        "public_repos": user.public_repos,
        "public_gists": user.public_gists,
        "total_stars": sum([repo.stargazers_count for repo in user.get_repos()]),
        "lines_of_code": get_lines_of_code(g),
        "bio": user.bio,
        "location": user.location,
        "company": user.company,
        "email": user.email,
        "website": user.blog,
        "hireable": user.hireable,
        "created_at": user.created_at.strftime("%d-%m-%Y"),
        "updated_at": user.updated_at.strftime("%d-%m-%Y"),
        "languages": get_languages(g),
        "total_commits": sum([repo.get_commits().totalCount for repo in user.get_repos() if not repo.fork]),
        "total_issues": sum([repo.get_issues().totalCount for repo in user.get_repos()]),
        "total_prs": sum([repo.get_pulls().totalCount for repo in user.get_repos()]),
    }
