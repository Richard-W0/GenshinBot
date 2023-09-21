# GenshinBot
 A bot that tracks resin and automatically notifies you
It sends a message an hour before your resin is full. The $$resin command also tells you how much resin you have and how long until its full.
You need to fill in your own bot token, account ltoken and ltuid. Heres how to get them

    Go to hoyolab.com.
    Login to your account.
    Press F12 to open Inspect Mode (ie. Developer Tools).
    Go to Storage, Cookies, https://www.hoyolab.com.
    Copy ltuid and ltoken.
I recommend putting this bot on a raspberry pi so you can have it running 24/7. There are some libraries that you need for this but they're all imported in bot.py so you can just run "pip install LibraryName" for each of the imported libraries to install them. Everything that you have to fill in is typed in all caps in the bot.py file.

Im no longer maintaining this as it has everything I need, but feel free to modify it to your liking, tho its a bit hard to implement anything new as it was designed to be a singe purpose bot.