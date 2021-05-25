#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot.translation import Translation # pylint: disable=import-error

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, update):
    
    buttons = [[
        InlineKeyboardButton('♻️𝑮𝑹𝑶𝑼𝑷', url='https://t.me/MovieNight120'),
        InlineKeyboardButton('𝑴𝑶𝑽𝑰𝑬 𝑵𝑰𝑮𝑯𝑻', url ='https://t.me/joinchat/HKLQU33m1l00NTI9')
    ],[
        InlineKeyboardButton('𝘾𝙝𝙖𝙣𝙣𝙚𝙡 📜', url='https://t.me/MovieNight124')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command("help") & filters.private)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home 🏠', callback_data='start'),
        InlineKeyboardButton('About 🤠', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command("about") & filters.private)
async def about(bot, update):
    buttons = [[
        InlineKeyboardButton('Home 🏠', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
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
