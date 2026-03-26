import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

OLD = "@MovSerColX"
NEW = "@The_Wolverine_Channel"

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if not msg:
        return

    if msg.video or msg.document:
        caption = msg.caption or ""

        caption = caption.replace(OLD, NEW)

        if NEW not in caption:
            caption += f"\n\nPowered by - {NEW}"

        if msg.video:
            await msg.reply_video(
                video=msg.video.file_id,
                caption=caption
            )
        elif msg.document:
            await msg.reply_document(
                document=msg.document.file_id,
                caption=caption
            )

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video)
)

print("🤖 Bot running...")
app.run_polling()
