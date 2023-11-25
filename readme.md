### Example
 ```python
import discord_self_embed

embed = discord_self_embed.Embed()
embed.set_title("title")
embed.set_title_url("url")
embed.set_description("description")
embed.set_color("#0BDB11")
embed.set_author("JaiFaim")
embed.set_author_url("url")
embed.set_image("url")

print(embed.generate_url())
 ```