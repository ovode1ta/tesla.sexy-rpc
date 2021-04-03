import os, requests, json
try:
    from pypresence import Presence # The simple rich presence client in pypresence
except:
    print("pypresence isn't installed, so im installing it right now (your welcome)")
    os.system("pip install pypresence")
    print("done B)")
try:
    import colorama
except:
    print("bruh colorama not installed")
    os.system("pip install colorama")
    print("done B))")
import time
import random
import json
import time
import requests
link = 'https://discordapp.com/api/guilds/814556675717595146/widget.json'
response = requests.get(link)
count = json.loads(response.text)
users = (count['presence_count'])
ping = os.popen('ping www.tesla.sexy -n 1')
result = ping.readlines()
msLine = result[-1].strip()
pingcool = msLine[-4:]
# 776945388606717962
client_id = "825105301141323819"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client



# How to get buttons
# Comment out Join, spectate, match, party_id, and party_size, and then uncomment the buttons thing 
# MAKE SURE TO DO FOR BOTH THINGS
# OR ELSE IT WONT WORK


RPC.connect()
RPC.update(
    large_image="tesla", small_image="tesla",
    small_text=".gg/transgender",
    join='6jLvKZfbliZT2xHieCDcNpPJcs2LHsAZBnp0jM3Fpo40Vf4Mt4Gi6ladapVoBVvO',
    spectate='Yxx2YFWYtptR5n1Vd5KEq3odpYkFK3od0W3M92IJ2Z212BWyY7xeZ4tqGqHMnlc1',
    match='eAcMLuL9YL9qhdrPs4rIBFqhBo4tKIX0GjUQZCcsOIEBHnmvDUt2wb24TESBQ63J',
    party_id='MO3ndQrMpxYnfyBUaeXkZawnzUgHfjqHhk1x3b3XfrG0OLOKzHQFTcZ307GneS6Y',
    party_size=[1,5],
    # buttons=[{"label": "Website", "url": "https://tesla.sexy"}, {"label": "Discord Server", "url": "https://discord.gg/ShCzNQAnV2"}], 
    details=f'Ping: {pingcool}',
    state=f'Members online: {users}')

print("made by cgd#5057 and pobg")

while True:
    time.sleep(5)
    RPC.update(
    large_image="tesla", small_image="tesla",
    small_text=".gg/transgender",
    join='6jLvKZfbliZT2xHieCDcNpPJcs2LHsAZBnp0jM3Fpo40Vf4Mt4Gi6ladapVoBVvO',
    spectate='Yxx2YFWYtptR5n1Vd5KEq3odpYkFK3od0W3M92IJ2Z212BWyY7xeZ4tqGqHMnlc1',
    match='eAcMLuL9YL9qhdrPs4rIBFqhBo4tKIX0GjUQZCcsOIEBHnmvDUt2wb24TESBQ63J',
    party_id='MO3ndQrMpxYnfyBUaeXkZawnzUgHfjqHhk1x3b3XfrG0OLOKzHQFTcZ307GneS6Y',
    party_size=[1,5],
    # buttons=[{"label": "Website", "url": "https://tesla.sexy"}, {"label": "Discord Server", "url": "https://discord.gg/ShCzNQAnV2"}], 
    details=f'Ping: {pingcool}',
    state=f'Members online: {users}')
