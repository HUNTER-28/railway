from pyrogram import Client, filters


bot = Client("TEST", api_id=11671020, api_hash="f3f57ad94ddd54bf92f4bcf7efc9a7b9", bot_token="1456016017:AAGjREqOnfrPPWxbZoUTyas7pKfjAWHz5vk")


@bot.on_message(filters.command("start"))
async def main(_, msg):
  await msg.reply_text("I'm Alive")


bot.run()
