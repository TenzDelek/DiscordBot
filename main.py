
import os
from dotenv import load_dotenv
from discord import Intents,Client,Message
from response import get_response
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = Intents.default()
intents.message_content = True  # This allows the bot to receive and process messages

client = Client(intents=intents)

#message function
async def send_message(message,user_message):
    if not user_message:
        print("message is empty")
        return
    if (is_private := user_message[0]=='?'):
        user_message=user_message[1:] #remove the ? 
    try:
        response=get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    username=str(message.author)
    user_message=message.content
    channel=str(message.channel)
    await send_message(message,user_message)
    # if message.content == "show":
    #     await message.channel.send(f'[{channel}] {username} : {user_message}')
    # print(f'[{channel}] {username} : {user_message}')
    # if message.content.startswith('yo'):
    #     await message.channel.send('tashi delek my boy')
    # if message.content == '$cho_khamsang':
    #     await message.channel.send('Tashi Delek')
 
def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()