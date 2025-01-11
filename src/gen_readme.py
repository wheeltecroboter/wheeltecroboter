import json
from src.draw_ascii import generate_logo
from src.fetch_info import fetch_stats
from github import Github

def generate_fetch(g:Github) -> str:
    with open("config.json", "r") as f:
        config = json.load(f)

    user = fetch_stats(g)
    pfp = generate_logo(g)


    stats = f"{user['username']}@github.com\n------------------------------\n"
    for stat in config['display_stats']:
        if stat in user:
            stats += f"{stat.replace('_', ' ').title()}: {user[stat]}\n"
    stats += f"\n{config['additional_info']}\n"

    pfp_lines = pfp.split("\n")
    stats_lines = stats.split("\n")

    max_lines = max(len(pfp_lines), len(stats_lines))
    pfp_lines += [""] * (max_lines - len(pfp_lines))
    stats_lines += [""] * (max_lines - len(stats_lines))

    combined = "\n".join(f"{pfp_line:<50} {stats_line}" for pfp_line, stats_line in zip(pfp_lines, stats_lines))
    
    return combined
    

def generate_readme(g:Github):
    content = generate_fetch(g)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)