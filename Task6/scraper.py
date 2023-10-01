import requests
from bs4 import BeautifulSoup


url = "https://www.espncricinfo.com/series/county-championship-division-one-2023-1347099/nottinghamshire-vs-middlesex-1347272/live-cricket-score"


response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")
    

    team1_name = soup.find("div", class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate !ds-text-typo-mid3").text
    team2_name = soup.find("div", class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate").text
    team1_score = soup.find("div", class_="ds-text-typo-mid3").text
    team2_score = soup.find("div", class_="ds-text-compact-m ds-text-typo ds-text-right ds-whitespace-nowrap fadeIn-exit-done").text
    match_summary = soup.find("div", class_="ds-text-tight-m ds-font-regular ds-truncate ds-text-typo").text
    
    live_scores_data = {
        "Team 1": team1_name,
        "Team 2": team2_name,
        "Team 1 Score": team1_score,
        "Team 2 Score": team2_score,
        "Summary": match_summary,
    }


else:
    print("Failed to retrieve cricket scores.")

