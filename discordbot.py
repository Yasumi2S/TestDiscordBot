import discord
import configparser

# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
# --------------------------------------------------
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')


# config.iniファイルの[DEFAULT]AccessTokenの値をアクセストークンとして設定
TOKEN = config_ini['DEFAULT']['AccessToken']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('Discordにログイン')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 検索実行
    #画像検索
    if message.content.startswith('!img '):
        #画像検索
        searchResalt = Img_Search(message)
        await message.channel.send(searchResalt)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

#------------
#画像検索処理
#------------
def Img_Search(message):
    #画像URLを作成
    word = message.replace('!img ','')
    url = 'https://www.google.com/search?hl=jp&q=' + message + '&btnG=Google+Search&tbs=0&safe=off&tbm=isch'
    return url