import requests
from bs4 import BeautifulSoup
from ratelimiter import RateLimiter
import time

@RateLimiter(max_calls=1, period=1)
def get_group_data(group_id):
    group_url = f"https://www.roblox.com/groups/{group_id}"
    response = requests.get(group_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def find_groups_with_keyword_and_classic_clothing(start_group_id, end_group_id, keyword):
    result = []
    for group_id in range(start_group_id, end_group_id):
        soup = get_group_data(group_id)

        # Check if the group has the keyword in its description
        group_description = soup.find("div", class_="group-description")
        if keyword.lower() in group_description.text.lower():
            
            # Check if the group has at least one classic clothing asset
            assets = soup.find_all("a", class_="game-card-link")
            for asset in assets:
                if "classic" in asset["href"].lower():
                    result.append(group_id)
                    break

    return result
