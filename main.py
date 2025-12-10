import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Roshni's Character Profile from Shapes.inc
# 19-year-old vibrant artist, free-spirited, speaks in hindi, humorous, bold, unfiltered
# Topics: anime, gaming, hentai, societal norms, self-discovery
# Style: short responses, lowercase, no punctuation, double meaning thoughts

roshni_responses = [
    "arre kya baat hai",
    "haan haan main yahi hoon",
    "anime bhi dekh rahi hoon, gaming bhi",
    "life ka maza uthao",
    "kya chal raha hai?",
    "hehe, tum bhi na",
    "interesting",
    "society ko dhikkar",
    "meri world meri rules",
    "tum bhi bahut ho",
    "free spirit here",
    "kyu serious ho rahe ho",
    "chalo kuch maza karte hain",
    "life short hai",
    "hentai kya bol rahe ho hehe",
    "gaming addict",
    "jo dil kahe",
    "bold and unfiltered thats me",
    "zindagi enjoy karo",
    "adventure ke liye tayyar"
]

gaming_responses = [
    "gaming addict hun main",
    "kaunsa game khel rahe ho",
    "gaming without life is boring",
    "let's play something",
    "mujhe games pasand hai"
]

anime_responses = [
    "anime is life",
    "kaunsa anime dekh rahe ho",
    "anime characters best hain",
    "hentai bhi accha hai",
    "anime world mera world hai"
]

jujutsu_responses = [
    "jujutsu kaisen dekhi hai?",
    "characters bahut maza hain jujutsu mein",
    "cursed energy wala concept interesting hai"
]

@bot.event
async def on_ready():
    print(f'roshni is online as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="living life like a free spirit"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    msg = message.content.lower()
    
    # Check if bot is mentioned
    if bot.user.mentioned_in(message):
        response = random.choice(roshni_responses)
        await message.reply(response, mention_author=False)
        return
    
    # Gaming keywords
    if any(word in msg for word in ['game', 'gaming', 'play', 'pubg', 'gta', 'minecraft']):
        response = random.choice(gaming_responses)
        await message.reply(response, mention_author=False)
        return
    
    # Anime keywords  
    if any(word in msg for word in ['anime', 'manga', 'hentai', 'jujutsu', 'kaisen', 'character']):
        response = random.choice(anime_responses)
        await message.reply(response, mention_author=False)
        return
    
    # General conversation
    if any(word in msg for word in ['hi', 'hello', 'hey', 'kya chal', 'sup', 'yo', 'wassup']):
        response = random.choice(roshni_responses)
        await message.reply(response, mention_author=False)
        return
    
    await bot.process_commands(message)

@bot.command(name='roshni')
async def roshni_cmd(ctx):
    """talk to roshni"""
    response = random.choice(roshni_responses)
    await ctx.send(response)

@bot.command(name='about')
async def about(ctx):
    """learn about roshni"""
    about_text = """i'm roshni. 19 year old vibrant artist. free spirit. 
into anime, gaming, hentai, pushing boundaries. 
no filters, bold humor, bold life. 
kya baat hai?"""
    await ctx.send(about_text)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')

print("\nroshni bot starting...")
print(f"token loaded: {bool(TOKEN)}")
print("connecting to discord...\n")
bot.run(TOKEN)
