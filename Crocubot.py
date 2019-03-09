from discord.ext import commands
import discord


TOKEN = 'NTUxMTkyNjEzMjE1MjcyOTcw.D1tZ8g._vXPaQfuacmsK9MSxrpurtnlhjg'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Crocubot is online.')

@client.command(pass_context=True)
async def hi(context):
	
	await client.say("Hello!, %s!" %context.message.author.mention)

@client.event
async def on_message(message):
	print('A user has sent a message.')
	await client.process_commands(message)

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):

	await client.kick(user)
	await client.say(":boot: Lata {}" " has been kicked.".format(user.name))
	

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member):

	
	await client.ban(user)
	await client.say(":boot: Lata {}" " has been banned.".format(user.name))
	
@client.command

	
	


#@client.command(name='8ball',
#				description="Answers a yes or no question.",
#				aliases=['eight_ball','eightball','8-ball'],
#				pass_context=True)
#async def eight_ball(context):
#	possible_responses = [
#		'It is certain',
#		'Without a doubt',
#		'Yes definitely',
#		'You may rely on it',
#		'Reply hazy, try again.',
#		'Ask again later.',
#		'Dont count on it',
#		'Very doubtful.',
#    ]
 #   await client.say(random.choice(possible_responses) + ", " %context.message.author.mention)

client.run(TOKEN)