if not checkModPerms(interaction.user):
  await interaction.response.send_message("You do not have permission to run this command!", ephemeral=True)
  return

try:
  id = int(user)
except:
  sentData = {
    "usernames": [
      user
    ],
    "excludeBannedUsers": False
  }
  data = requests.post("https://users.roblox.com/v1/usernames/users", json=sentData).json()
  id = data['data'][0]['id']

url = f"https://users.roblox.com/v1/users/{str(id)}"
data = requests.get(url).json()
thumbUrl = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={str(id)}&size=150x150&format=Png&isCircular=false"
thumbData = requests.get(thumbUrl).json()

embed = discord.Embed(
  title = data['displayName'],
  timestamp = datetime.now()
)

embed.add_field(name="Username", value=data['name'], inline=False)
embed.add_field(name="Description", value=data['description'], inline=False)
embed.add_field(name="Created", value=f"<t:{int(datetime.fromisoformat(str(data['created'])).timestamp())}:R>", inline=True)

if data['isBanned']:
  embed.add_field(name="🔴 Banned!",value="",inline=False)
if data['hasVerifiedBadge']:
  embed.add_field(name="✔️ Verified!",value="",inline=False)

embed.set_thumbnail(url=thumbData['data'][0]['imageUrl'])

await interaction.response.send_message(embed=embed)