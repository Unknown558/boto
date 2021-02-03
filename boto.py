from discord.ext import commands



TOKEN = "ODA2Mjk3MzQ0MDk3OTEwODQ0.YBnY6w.693TAMEFDws1Vyx3VZuOtdO57YM"


bot = commands.Bot(command_prefix='?')

@bot.command(name='avise', help="avise os membros comuns")
async def on_message(message):
	if message.author == bot.user:
		return

	print("AAvc")
	response = """Você foi avisado ̿'̿'\\̵͇̿̿\\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿  
	https://cdn.discordapp.com/attachments/806303792139075605/806318291794264074/15b5f3773208f4bd92e2387c87bc0bb382fad8b4f90cb7e32c3c581800a1acd6_1.png"""
	await message.send(response)

@bot.command(name='desavise', help="desavise os membros comuns")
async def on_message(message):
	if message.author == bot.user:
		return

	print("AAvc")
	response = "Você foi desavisado ̿'̿'\\̵͇̿̿\\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿  "
	await message.send(response)

@bot.command(name='diga', help="diga aos membros comuns")
async def on_message(message, *a):
	if message.author == bot.user:
		return
	print(message.author)
	palavra = ""
	for i in a:
		palavra = palavra + i + " "

	print("AAvc")
	response = palavra
	await message.send(response)

@bot.command(name="tatakae", help="diga para os membros lutarem por Você")
async def on_message(message, *a):
	if message.author == bot.user:
		return

	response = "https://cdn.discordapp.com/attachments/806303792139075605/806320827825258536/00d1d624-281d-4818-a1c8-3e4ede69b79d.png"
	await message.send(response)



bot.run(TOKEN)
