import json
import logging
from pathlib import Path
import random

import discord
from discord.ext import commands

from bot.constants import Colours


log = logging.getLogger(__name__)


class TechLeaders(commands.Cog):
    """ A """

    def __init__(self, bot):
        self.bot = bot
        self.leaders = self.tech_json()


    def tech_leaders_pfp(self):
        """grabs the image file of the tech leader"""
        pass

    def tech_json(self):
        """grabs the write up for the tech leaders"""
        leaders = open(Path('bot', 'resources', 'pride', 'techleader.json'), 'r')
        return json.load(leaders)

    async def tech_embeds(self):
        leader = random.choice(self.leaders)
        leader_name = leader["name"]
        leader_desc = leader["description"]
        leader_photo = leader["image"]

    @commands.command()
    async def prideleader(self, ctx):

        leader = random.choice(self.leaders)
        leader_name = leader["name"]
        leader_desc = leader["description"]
        leader_photo = leader["image"]
        file = discord.File(open("bot/resources/Pride/TechPeople","rb"))
        e = discord.Embed(title=leader_name, description=leader_desc, colour=Colours.blue)
        e.set_thumbnail(url=leader_photo)
        await ctx.send(file=file,embed=e)


def setup(bot):
    """ cog"""
    bot.add_cog(TechLeaders(bot))
    log.info("Techleader cog loaded")


