import discord
import responses
import os
import requests
import json
import asyncio
import genshinstats as gs
import time

async def send_message(channel, content):
    try:
        await channel.send(content)
    except Exception as e:
        print(e)

async def check_resin(client, user_info):
    uid = user_info["uid"]
    ltuid = user_info["ltuid"]
    ltoken = user_info["ltoken"]
    user_name = user_info["name"]
    message_sent = False
    last_message_time = 0
    
    while not client.is_closed():
        gs.set_cookie(ltuid=ltuid, ltoken=ltoken)
        notes = gs.get_notes(uid)
        current_resin = notes['resin']

        if current_resin in [152, 153]:
            channel = client.get_channel(YOUR CHANNEL ID)
            
            
            if not message_sent:
                if user_name == "YOUR NAME":
                    await send_message(channel, f"{user_name}'s resin count is at {current_resin}. You have about an hour until it's full.")
                elif user_name == "ANOTHER NAME":
                    await send_message(channel, f"{user_name}'s resin is at {current_resin}. You have about an hour until it's full.")
                
                
                message_sent = True
                last_message_time = time.time()
        else:
            
            message_sent = False

        await asyncio.sleep(7 * 60)  



def run_discord_bot():
    TOKEN = "YOUR TOKEN"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    user_info = [
        {"uid": YOUR USER ID, "ltuid": YOUR LTUID, "ltoken": "YOUR LTOKEN", "name": "YOUR NAME"},
        {"uid": ANOTHER USER ID, "ltuid": ANOTHER LTUID, "ltoken": "ANOTHER LTOKEN", "name": "ANOTHER NAME"}
        
    ]

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

        
        for user in user_info:
            client.loop.create_task(check_resin(client, user))

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print(f'{username} said: "{user_message}" ({channel})')

            prefix = "$"
            if user_message.startswith(prefix):
                command = user_message[len(prefix):].strip()  
                await send_message(message.channel, responses.handle_response(command, user_info))
    
    client.run(TOKEN)
