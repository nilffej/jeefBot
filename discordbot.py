import discord

client = discord.Client()

def check_im(str):
    return str.lower() == 'im' or str.lower() == 'i\'m'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    firstword = message.content[:message.content.find(' ')]
    afterfirst = message.content.find(' ')
    print(message.content)
    print(afterfirst)
    print('\n')
    if check_im(firstword) and afterfirst:
        await message.channel.send('Hi{}, I\'m jeefBot!'.format(message.content[afterfirst:]))

client.run('NzcwODY2MjgyMjYyMjk4NjQ1.X5jzKw.-u3mLXirmgFPlYi4KzVbiQs9AZ4')