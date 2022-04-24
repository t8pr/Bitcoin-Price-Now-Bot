import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix="$", case_insensitive=True)

rs = requests.session()
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
gif = 'https://c.tenor.com/GNZKiEbbiqkAAAAC/bitcoin-blockchain.gif'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Info : $info"))
    print(f"[+] I Joined To Discord -> {client.user}")

@client.command()
async def info(ctx):
    inf_embed = discord.Embed(title="```Bot information```", color=0xBD9B4B)
    inf_embed.set_thumbnail(url=f"{gif}")
    inf_embed.add_field(name="** **", value="`$btc` ** -> For See Btc Price **", inline=False)
    inf_embed.add_field(name="** **", value="`$dev` ** -> Info About Developer **", inline=False)
    inf_embed.add_field(name="** **", value="`$ping` ** -> For See Bot Ping **", inline=False)
    await ctx.send(embed=inf_embed)

@client.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="Bitcoin Price Ping", description=f"**This Bitcoin Price Now Bot Ping : {round(client.latency*1000)} ms**", color=0x167F93)
    await ctx.send(embed=ping_embed)

@client.command()
async def dev(ctx):
    dev_embed = discord.Embed(title="Developer Bot", description=f"**This Price Master Bot Programmed By 8PR**", color=0xffffff)
    dev_embed.add_field(name="Website", value="https://8pr.club", inline=True)
    dev_embed.add_field(name="instagram", value="[T8PR](https://www.instagram.com/t8pr)", inline=True)
    await ctx.send(embed=dev_embed)

@client.command()
async def btc(ctx):
    for _ in range(1):
        try:
            btc_req = rs.get(url).json()
        except Exception as errcon:
            await ctx.send(f'Error Request -> {errcon}')
            break
        try:
            usd = str(btc_req['bpi']['USD']['rate'])
            gbp = str(btc_req['bpi']['GBP']['rate'])
            eur = str(btc_req['bpi']['EUR']['rate'])
        except Exception as errget:
            await ctx.send(f'Error Get Bitcoin Price -> {errget}')
            break
        btc_embad = discord.Embed(title="```Bitcoin Price Now```", color=0xE29F05)
        btc_embad.set_thumbnail(url=f"{gif}")
        btc_embad.add_field(name="** **", value=f"`USD` ** -> {usd} **", inline=False)
        btc_embad.add_field(name="** **", value=f"`GBP` ** -> {gbp} **", inline=False)
        btc_embad.add_field(name="** **", value=f"`EUR` ** -> {eur} **", inline=False)
        await ctx.send(embed=btc_embad)
    

client.run('OTU5NzgwODMxMDM4MTYwOTI2.Ykg3jQ.kdf02XZS9Ri2Lot78F9vYt6fkoY')