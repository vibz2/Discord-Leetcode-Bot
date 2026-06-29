import discord

from database import clear_all_data


class ConfirmClearAllView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.button(
        label="Confirm",
        style=discord.ButtonStyle.danger
    )
    async def confirm(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        deleted = clear_all_data()

        await interaction.response.edit_message(
            content=f"Deleted {deleted} records.",
            view=None
        )

    @discord.ui.button(
        label="Cancel",
        style=discord.ButtonStyle.secondary
    )
    async def cancel(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.edit_message(
            content="Operation cancelled.",
            view=None
        )