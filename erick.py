import urllib.request
import json
from config import auth_token


# Get the war preference for each member in the clan
def get_war_preference(player_tag):
    # player_uri = f"https://api.clashofclans.com/v1/players/%23{player_tag}"
    player_uri = "https://api.clashofclans.com/v1/players/{}".format(player_tag.replace("#", "%23"))
    headers = {"Authorization": f"Bearer {auth_token}"}
    player_request = urllib.request.Request(player_uri, headers=headers)

    with urllib.request.urlopen(player_request) as player_response:
        player_data = json.loads(player_response.read().decode('utf-8'))
        war_preference = player_data.get("warPreference", "N/A")
        return war_preference


# Get all player tags from the clans endpoint and return tag and war preference from above function
def get_all_player_tags_from_clan(clan_tag):
    clan_uri = f"https://api.clashofclans.com/v1/clans/%23{clan_tag}"
    print("Querying", clan_uri)

    headers = {"Authorization": f"Bearer {auth_token}"}
    clan_request = urllib.request.Request(clan_uri, headers=headers)

    with urllib.request.urlopen(clan_request) as clan_response:
        json_data = json.loads(clan_response.read().decode('utf-8'))

        member_list = json_data.get("memberList", [])
        for member in member_list:
            player_tag = member.get("tag", "N/A")
            war_preference = get_war_preference(player_tag)
            print(f"Player Tag: {player_tag}", f"War Preference: {war_preference}")


def get_clan_tag():
    # clan_tag = input("Clan Tag: ")
    clan_tag = '8JGG22CJ'
    get_all_player_tags_from_clan(clan_tag)


get_clan_tag()
