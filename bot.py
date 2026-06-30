import os

import discord

from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv

from db import (
    init_db,
    add_solution,
    get_leaderboard,
    get_user_stats,
)
from views.confirm_clear_all import ConfirmClearAllView
from views.confirm_clear_user import ConfirmClearUserView


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError(
        "DISCORD_TOKEN not found in .env"
    )

init_db()

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()

        print(f"Synced {len(synced)} commands.")
        for cmd in bot.tree.get_commands():
            print(cmd.name)

    except Exception as e:
        print(e)


@bot.tree.command(
    name="solve",
    description="Log a solved LeetCode problem."
)
async def solve(
    interaction: discord.Interaction,
    problem_id: int,
    difficulty: str
):
    success, result = add_solution(
        interaction.user.id,
        interaction.user.display_name,
        problem_id,
        difficulty
    )

    if success:
        await interaction.response.send_message(
            f"YIPPEE! Logged problem #{problem_id}\n"
            f"+{result} points awarded."
        )
    else:
        await interaction.response.send_message(
            f"ERR You got something wrong mister! {result}",
            ephemeral=True
        )


@bot.tree.command(
    name="leaderboard",
    description="View server leaderboard."
)
async def leaderboard(
    interaction: discord.Interaction
):
    rows = get_leaderboard()

    if not rows:
        await interaction.response.send_message(
            "No solves have been logged yet."
        )
        return

    message = "**Leaderboard**\n\n"

    for index, (
        username,
        points
    ) in enumerate(rows, start=1):

        message += (
            f"{index}. "
            f"**{username}** "
            f"- {points} pts\n"
        )

    await interaction.response.send_message(
        message
    )


@bot.tree.command(
    name="stats",
    description="View your solve statistics."
)
async def stats(
    interaction: discord.Interaction
):
    stats_data = get_user_stats(
        interaction.user.id
    )

    embed = discord.Embed(
        title=f"{interaction.user.display_name}'s Stats"
    )

    embed.add_field(
        name="Total Solves",
        value=stats_data["solves"],
        inline=False
    )

    embed.add_field(
        name="Points",
        value=stats_data["points"],
        inline=False
    )

    embed.add_field(
        name="Easy",
        value=stats_data["easy"]
    )

    embed.add_field(
        name="Medium",
        value=stats_data["medium"]
    )

    embed.add_field(
        name="Hard",
        value=stats_data["hard"]
    )

    await interaction.response.send_message(
        embed=embed
    )

@bot.tree.command(
    name="clear_user",
    description="Remove all solves for a user."
)
@app_commands.default_permissions(
    administrator=True
)
async def clearuser(
    interaction: discord.Interaction,
    user: discord.Member
):
    await interaction.response.send_message(
        f"CAUTION!! This will delete all data for {user.display_name}.",
        view=ConfirmClearUserView(user),
        ephemeral=True
    )

@bot.tree.command(
    name="clear_all",
    description="Remove all solve data."
)
@app_commands.default_permissions(
    administrator=True
)
async def clearall(
    interaction: discord.Interaction
):
    await interaction.response.send_message(
        "CAUTION!! This will delete all solve data.",
        view=ConfirmClearAllView(),
        ephemeral=True
    )

@bot.tree.command(
    name="sync",
    description="Sync LeetCode solves."
)
async def sync(
    interaction: discord.Interaction
):
    try:
        result = sync_user(
            interaction.user.id
        )

        await interaction.response.send_message(
            f"Sync complete!\n\n"
            f"Imported: {result['imported']}\n"
            f"Skipped: {result['skipped']}\n"
            f"Points Earned: {result['points']}"
        )

    except ValueError as e:
        await interaction.response.send_message(
            str(e),
            ephemeral=True
        )


bot.run(TOKEN)