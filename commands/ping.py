latency = round(bot.latency * 1000)
if latency < 100:
  color = discord.Color.green()
  status = "Excellent"
elif latency < 200:
  color = discord.Color.yellow()
  status = "Good"
else:
  color = discord.Color.red()
  status = "Poor"

embed = discord.Embed(
  title = "🏓 Pong!",
  color = color,
  timestamp = datetime.utcnow()
)

embed.add_field(name="Latency", value=f"{latency}ms", inline=True)
embed.add_field(name="Status", value=status, inline=True)
embed.set_footer(text="Gator Games")

await interaction.response.send_message(embed=embed)