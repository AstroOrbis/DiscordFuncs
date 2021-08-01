from discord_webhook import DiscordWebhook

class Webhook:
  def sendMessage(url, content):
    webhook = DiscordWebhook(url=url, content=content)
    webhook.execute()