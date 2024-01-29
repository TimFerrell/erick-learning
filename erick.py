import urllib.request
import json
from config import auth_token


def get_all_player_tags_from_clan(clan_tag):
    clan_uri = f"https://api.clashofclans.com/v1/clans/%23{clan_tag}"
    print("Querying", clan_uri)

    headers = {"Authorization": f"Bearer {auth_token}"}
    request = urllib.request.Request(clan_uri, headers=headers)

    with urllib.request.urlopen(request) as response:
        json_data = json.loads(response.read().decode('utf-8'))

        clan_name = json_data.get("name", "N/A")
        print(f"Clan Name: {clan_name}")


def get_clan_tag():
    # clan_tag = input("Clan Tag: ")
    clan_tag = '8JGG22CJ'
    get_all_player_tags_from_clan(clan_tag)


get_clan_tag()
