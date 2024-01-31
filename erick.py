import urllib.request
import json
from config import auth_token
from google.oauth2.service_account import Credentials
import gspread
from tqdm import tqdm
import datetime

# Set variables
credentials_path = './clash-of-clans-408313-6f7d5bc0eab1.json'
spreadsheet_key = '1BAo-heHsljwPdtlUs1PPSbYqXEpHUR4taDugDWtdC3k'
sheet_title = 'Clan Data'
sheet_title_datetime = 'Date_Time'


# Get the war preference for each member in the clan
def get_war_preference(player_tag):
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
        player_data_list = []

        with tqdm(total=len(member_list), desc="Querying MemberList") as pbar:
            for member in member_list:
                player_data_dict = {
                    'Name': member["name"],
                    'Player Tag': member["tag"],
                    'Player Role': member["role"]
                }

                # Append the formatted data to the list
                player_data_list.append(player_data_dict)

                pbar.update(1)

        # Return the list for writing to the sheet
        return player_data_list


def write_to_sheet(player_data_list):
    # Load Google Sheets API credentials from JSON file
    creds = Credentials.from_service_account_file(credentials_path,
                                                  scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Connect to the Google Sheet by title
    sheet = gspread.authorize(creds).open_by_key(spreadsheet_key).worksheet(sheet_title)

    # Clear the sheet
    sheet.clear()

    # Set headers
    headers = list(player_data_list[0].keys())
    print("Headers:", headers)

    values = list(player_data_list[0].values())
    print("Values:", values)

    sheet.append_row(headers)

    # Use tqdm to create a progress bar for the loop
    with tqdm(total=len(player_data_list), desc="Writing data to Google Sheet") as pbar:
        # Batch update rows
        sheet.append_rows(player_data_list)
        pbar.update(len(player_data_list))  # Update the progress bar for each batch


def write_date_time_to_sheet():
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Load Google Sheets API credentials from JSON file
    creds = Credentials.from_service_account_file(credentials_path,
                                                  scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Connect to the Google Sheet by title
    sheet = gspread.authorize(creds).open_by_key(spreadsheet_key).worksheet(sheet_title_datetime)

    # Clear the sheet
    sheet.clear()

    # Set headers
    headers = ["Last Updated"]
    sheet.append_row(headers)

    # Write date/time stamp
    sheet.update_acell('A2', current_datetime)
    # sheet.append_rows(current_datetime)


def get_clan_tag():
    clan_tag_input = input("Enter Clan Tag: ").strip()  # Remove any leading or trailing white space

    if "#" in clan_tag_input:
        clan_tag = clan_tag_input.split("#")[1]  # Strip out the # in the clan tag
    else:
        clan_tag = clan_tag_input
    # clan_tag = '8JGG22CJ'
    write_to_sheet(get_all_player_tags_from_clan(clan_tag))
    write_date_time_to_sheet()


get_clan_tag()

# To Do:
# 1. Add error handling
# 2. Add more documentation
# 3. Add progress bar for read back?
