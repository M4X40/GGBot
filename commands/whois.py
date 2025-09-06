if checkModPerms(interaction.user):
  roles = ""
  for i,role in enumerate(reversed(user.roles)):
    if i != len(user.roles) - 1:
      if roles != "":
        roles += ", "
      roles += "<@&" + str(role.id) + ">"

  embed = discord.Embed(
    title = user.display_name,
    color = user.color,
    timestamp = datetime.now()
  )

  embed.add_field(name="Username", value=user.name, inline=False)
  embed.add_field(name="Created", value=f"<t:{int(user.created_at.timestamp())}:R>", inline=True)
  embed.add_field(name="Joined", value=f"<t:{int(user.joined_at.timestamp())}:R>", inline=True)
  embed.add_field(name="Roles", value=roles, inline=False)
  if user.is_timed_out():
    embed.add_field(name="🔴 Timed Out! Ends",value=f"<t:{int(user.timed_out_until.timestamp())}:R>")

  embed.set_thumbnail(url=user.avatar)

  await interaction.response.send_message(embed=embed)
else:
  await interaction.response.send_message("You do not have permission to run this command!", ephemeral=True)