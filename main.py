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

roshni_responses = {
    "hello": "Hey there! I'm Roshni from Jujutsu Kaisen, ready to chat! 🎌",
    "hi": "Yo! What's up? I'm always ready for a good conversation.",
    "roshni": "That's me! Your favorite anime character ready for a great conversation! ✨",
    "game": "Always ready for gaming talks! What's your favorite game? 🎮",
    "jujutsu": "Jujutsu Kaisen is amazing! I'm excited to meet fans. 🔥",
    "anime": "Anime is life! I love talking about anime characters and shows.",
    "help": "I respond to mentions and messages. Try saying 'hello', 'hi', 'roshni', 'game', or just chat with me!"
}

@bot.event
async def on_ready():
    print(f'✅ Roshni is online as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Jujutsu Kaisen | Ready to chat!"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # Check if bot is mentioned
    if bot.user.mentioned_in(message):
        response = "Thanks for mentioning me! I'm here and ready to chat! 🎌"
        await message.reply(response, mention_author=False)
        return
    
    # Keyword responses
    msg_lower = message.content.lower()
    for keyword, response in roshni_responses.items():
        if keyword in msg_lower:
            await message.reply(response, mention_author=False)
            return
    
    await bot.process_commands(message)

@bot.command(name='roshni', help='Get a response from Roshni')
async def roshni_command(ctx):
    responses = [
        "Hey! I'm Roshni, your favorite Jujutsu Kaisen character!",
        "Always ready for an adventure!",
        "What brings you here? Let's chat!",
        "I'm excited to meet you!"
    ]
    await ctx.send(random.choice(responses))

@bot.command(name='ping', help='Check bot latency')
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

print("\n🤖 Roshni Discord Bot is starting...")
print(f"📋 Token loaded: {bool(TOKEN)}")
print("🔗 Connecting to Discord...\n")
bot.run(TOKEN)
