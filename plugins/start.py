from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/whiteeyebots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/mrdayamzaidibot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n I Am WhiteEye-YouTubeBot I Can Download Any Video Of Youtube Do /help for More info. Join The Channel Given below For My Use"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
