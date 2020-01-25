import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
	print('ready up!')
	print(bot.user.name)
	print(bot.user.id)
	bot.run('jDbcV-6fHtrKunOqooTAvWZ_ArhK4c_3')
