#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @lnc3f3r Jins Mathew Re-Create

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from .. import OWNER_ID

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"{file_name} \n @parkboyschat",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐ญ โ๐๐ฃ๐ ๐๐ ๐ง๐๐๐ค ๐', url="https://t.me/parkboyschat"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/joinchat/TRlZZilyh-MVa66t'),
        InlineKeyboardButton('Source Code ๐งพ', url ='https://t.me/joinchat/YS-WlsUC9nFiOWM0')
    ],[
        InlineKeyboardButton('Support ๐ ', url='https://t.me/joinchat/YS-WlsUC9nFiOWM0')
    ],[
        InlineKeyboardButton('Help โ', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    if update.from_user.id not in OWNER_ID:
        await bot.send_message(
            chat_id=update.chat.id,
            text="""<b>Hey {}!!</b>
            เด เดฌเตเดเตเดเต <b><u><a href="https://t.me/joinchat/TRlZZilyh-MVa66t">Universal Film Studio Group</a></u></b> เดฒเตเดเตเดเต เดเดณเตเดณเดคเต เดเดจเตเดจเต เดเดจเดฟ เดตเตเดฃเตเดเตเด เดตเตเดฃเตเดเตเด เดชเดฑเดฏเดฃเต??
            เดเดชเตเดชเต เดชเดฟเดจเตเดจเต เดเดจเตเดคเดฟเดจเดพ เดตเตเดฃเตเดเตเด เดตเตเดฃเตเดเตเด เดธเตเดฑเตเดฑเดพเตผเดเตเดเต เดเตเดคเตเดคเดฟ เดเดณเดฟเดเตเดเดพเตป เดตเดฐเตเดจเตเดจเต... เด เดธเตเดกเดฟเดฒเตเดเตเดเต เดเดเตเดเดพเดจเตเด เดฎเดพเดฑเดฟ เดเดฐเดฟเดเตเดเตโ เดเดจเดฟ๐คญ๐คญ""".format(update.from_user.first_name),
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
        return
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home โก', callback_data='start'),
        InlineKeyboardButton('About ๐ฉ', callback_data='about')
    ],[
        InlineKeyboardButton('Close ๐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    if update.from_user.id not in OWNER_ID:
        await bot.send_message(
            chat_id=update.chat.id,
            text="""<b>Hey {}!!</b>
            เดจเต เดเดคเดพ..... เดเดจเตเดจเต เดชเตเดเตเดฏเต เดเดตเตป help เดเตเดฏเตเดเตเดเต เดตเดจเตเดจเดฟเดฐเดฟเดเตเดเตเดจเตเดจเต๐ค...I'm Different Bot U Know""".format(update.from_user.first_name),
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
        return
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home โก', callback_data='start'),
        InlineKeyboardButton('Close ๐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
