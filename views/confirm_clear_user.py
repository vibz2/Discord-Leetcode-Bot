import discord

from database import clear_user_data

class ConfirmClearUserView(discord.ui.View):
    def __init__(self, user: discord.Member):
        super().__init__(timeout=60)
        self.user = user

    @discord.ui.button(
        label="Confirm",
        style=discord.ButtonStyle.danger
    )
    async def confirm(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        deleted = clear_user_data(self.user.id)

        await interaction.response.edit_message(
            content=(f"BYE BYE! Deleted {deleted} records."
                     f"for {self.user.display_name}"),
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