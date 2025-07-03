from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# .env 파일 불러오기
load_dotenv()

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = int(os.environ['CHANNEL_ID'])
TARGET_GROUP_ID = int(os.environ['TARGET_GROUP_ID'])

async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.id == CHANNEL_ID:
        await context.bot.forward_message(
            chat_id=TARGET_GROUP_ID,
            from_chat_id=CHANNEL_ID,
            message_id=update.channel_post.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_channel_post))

app.run_polling()
