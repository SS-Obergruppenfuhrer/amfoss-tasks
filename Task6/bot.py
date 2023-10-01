import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="livescore")
async def get_live_scores(ctx):

    url = "https://www.espncricinfo.com/series/county-championship-division-one-2023-1347099/nottinghamshire-vs-middlesex-1347272/live-cricket-score"
    

    response = requests.get(url)
    

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        

        team1_name = soup.find("div", class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate !ds-text-typo-mid3").text
        team2_name = soup.find("div", class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate").text
        team1_score = soup.find("div", class_="ds-text-typo-mid3").text
        team2_score = soup.find("div", class_="ds-text-compact-m ds-text-typo ds-text-right ds-whitespace-nowrap fadeIn-exit-done").text
        match_summary = soup.find("div", class_="ds-text-tight-m ds-font-regular ds-truncate ds-text-typo").text
    
        

        await ctx.send(f"Team 1: {team1_name} - {team1_score}\nTeam 2: {team2_name} - {team2_score}\nSummary: {match_summary}")
    else:
        await ctx.send("Failed to retrieve cricket scores. Try again later.")


@bot.command(name="generate")
async def generate_csv(ctx):

    live_scores_data = [
        {
        "Team 1": team1_name,
        "Team 2": team2_name,
        "Team 1 Score": team1_score,
        "Team 2 Score": team2_score,
        "Summary": match_summary,
        }
    ]
    

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    

    csv_filename = f"live_scores_{timestamp}.csv"
    

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Team 1", "Team 2", "Team 1 Score", "Team 2 Score", "Summary"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        

        writer.writeheader()
        

        writer.writerows(live_scores_data)
    

    await ctx.send(f"CSV file generated: {csv_filename}")


@bot.command(name="bot_help")
async def help_commands(ctx):

    help_message = """
    !livescore - Get live cricket scores
    !generate - Generate a CSV file of live scores
    !bot_help - Display this help message
    """
    

    await ctx.send(help_message)


bot.run(DISCORD_TOKEN)







