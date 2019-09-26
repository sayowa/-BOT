import discord
from discord.ext import commands
import os
import asyncio
from datetime import datetime, timedelta

client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 625656760501272617 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(625682764431097861)
        if before.channel is None: 
            msg = f'おっと？{now:%H:%M} に {member.name} が {after.channel.name} に参加したみたいですよ。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'おや？{now:%H:%M} に {member.name} が {before.channel.name} から退出してしまったみたいですね。'
            await alert_channel.send(msg)
            
@client.event
async def on_member_join(member):
    guild = member.guild # サーバー
    sysch = guild.system_channel # 参加メッセージを表示するチャンネル
    if sysch: # チャンネルが設定されてなかったら何もしない
        text = f'{member.mention} さん　いらっしゃいませ。お約束のテキストチャンネル読んでくださいね。'
        await sysch.send(text)

@client.event
async def on_member_remove(member):
    guild = member.guild # サーバー
    sysch = guild.system_channel # 参加メッセージを表示するチャンネル
    if sysch: # チャンネルが設定されてなかったら何もしない
        text = f'{member.name} さん　寂しいですが、またよかったら来てくださいね'
        await sysch.send(text)
        
client.run(token)

