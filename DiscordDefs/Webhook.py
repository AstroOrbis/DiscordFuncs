from discord_webhook import DiscordWebhook

def sendMessage(url, content):
  webhook = DiscordWebhook(url=url, content=content)
  webhook.execute()