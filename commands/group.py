  url = "https://groups.roblox.com/v1/groups/5977288"
  thumbUrl = "https://thumbnails.roblox.com/v1/groups/icons?groupIds=5977288&size=150x150&format=Png&isCircular=true"
  data = requests.get(url).json()
  thumbData = requests.get(thumbUrl).json()
  
  # Basic data
  name = data['name']
  desc = data['description']
  memb = data['memberCount']
  thumb = thumbData['data'][0]["imageUrl"]
  
  # Shout stuff
  shoutUser = data['shout']['poster']['username']
  shoutBody = data['shout']['body']
  
  # Embed setup
  embed = discord.Embed(
    title = name,
    url="https://www.roblox.com/communities/5977288/Gator-Games-GG",
    description = desc,
    color = discord.Color.green(),
    timestamp = datetime.now(),
  )
  
  embed.set_thumbnail(url=thumb)
  embed.add_field(name="Members", value=memb)
  embed.add_field(name="Shout", value=f"{shoutUser}: {shoutBody}", inline=False)
  
  
  await interaction.response.send_message(embed=embed)
