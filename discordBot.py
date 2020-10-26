import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)


messageList = []
userList = []
ans = []
stimulus = []

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    messageList.append(message.content)
    userList.append(message.author.name)

    
    if userList[0] == 'TARGET':
        ans.append(messageList[0])
        messageList.pop(0)
        userList.pop(0)
    else:
        if message.author != "BOT":
            stimulus.append(messageList[0])
            messageList.pop(0)
        

    if len(messageList) == 5:
        messageList.pop(0)
        #print(messageList)
    if len(userList) == 5:
        userList.pop(0)
        #print(userList)
    if message.author.name == "YOURNAME":
        if message.content == "dumpData":
            with open("Answers.txt", "w") as output:
                output.write(str(ans))
            with open("Stimulus.txt", "w") as output:
                output.write(str(stimulus))
            await message.channel.send("Data dumped to storage.")
    
client.run(TOKEN)
