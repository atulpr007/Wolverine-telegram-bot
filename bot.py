from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

OLD = "@MovSerColX"
NEW = "@The_Wolverine_Channel"

TOKEN = "8245817710:AAGufmsCeZTDnqqdI6okAeldJbyY5OE-VGk"

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if not msg:
        return

    if msg.video or msg.document:
        caption = msg.caption or ""

        # Replace username
        caption = caption.replace(OLD, NEW)

        # Add if not present
        if NEW not in caption:
            caption += f"\n\nPowered by - {NEW}"

        # Make full bold
        caption = f"<b>{caption}</b>"

        if msg.video:
            await msg.reply_video(
                video=msg.video.file_id,
                caption=caption,
                parse_mode="HTML"
            )
        elif msg.document:
            await msg.reply_document(
                document=msg.document.file_id,
                caption=caption,
                parse_mode="HTML"
            )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video)
)

print("🤖 Bot running...")
app.run_polling()app.add_handler(
    MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video)
)

print("🤖 Bot running...")
app.run_polling()
