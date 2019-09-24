import discord
from discord.ext import commands
import os
import asyncio

# 通知用のチャンネルID
inform_channel = 625682764431097861

token = os.environ['DISCORD_BOT_TOKEN']

# bot
bot = Discordrb::Commands::CommandBot.new token: TOKEN, client_id: CLIENT_ID, prefix:'/'

# 誰かがvoice channelに出入りしたら発火
bot.voice_state_update do |event|
    # 発火させたユーザー名を取得
    user = event.user.name

    # もしデータが空だと抜けていったチャンネルを取得
    if event.channel == nil then
        # チャンネル名を取得
        channel_name = event.old_channel.name

        # 退出したことをinform_channelに通知
        bot.send_message(inform_channel, "@everyone #{user} が #{channel_name}を出たで～")
    else
        # チャンネル名を取得
        channel_name = event.channel.name

        # 入室したことをinform_channelに通知
        bot.send_message(inform_channel, "@everyone #{user} が #{channel_name}に入ったで～")
    end
end

client.run(token)

