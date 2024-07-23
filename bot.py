import os
import subprocess
import discord
from discord.ext import commands

TOKEN = 'replace_with_bot_token'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command(name='run')
async def run_command(ctx):
    bash_command = 'replace_with_bash_command'

    try:
        result = subprocess.run(bash_command, shell=True, check=True, text=True, capture_output=True)
        output = result.stdout if result.stdout else 'Command executed successfully.'
    except subprocess.CalledProcessError as e:
        output = e.stderr if e.stderr else 'An error occurred while executing the command.'

    await ctx.send(f'```\n{output}\n```')

bot.run(TOKEN)
