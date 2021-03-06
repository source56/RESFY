# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐๐ป **ููุง ุญุจ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ุงูุง ุฑูุจูุช ูุชุดุบูู ุงูููุณููู ูุงูููุฏูู ุนูู ููุตุฉ ุชููุฌุฑุงู!**

๐ **ููุนุฑูุฉ ุงูุงูุฑ ูุฐุง ุงูุจูุช ุงุถุบุท ุนูู ยป ุงูุงูุงูุฑ ุงูุงุณุงุณูุฉ!**

๐ **ููุนุฑูุฉ ุทุฑููุฉ ุชุดุบูู ูุฐุง ุงูุจูุช ุงุถุบุท ุนูู ยป ุทุฑููุฉ ุงูุชุดุบูู!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ุงุถููู ุงูู ูุฌููุนุชู โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("ุทุฑููุฉ ุงูุชุดุบูู", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("ุงูุงูุงูุฑ ุงูุงุณุงุณูุฉ", callback_data="cbcmds"),
                    InlineKeyboardButton("ุงููุทูุฑ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ ูุฑูุจ ุงูุณูุฑุณ ๐", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ ุชุญุฏูุซุงุช ุงูุจูุช ๐", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐๐๐๐ถ๐ธ ๐ถ๐b๐๐ด ๐", url="https://t.me/VFF35"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ **ูุฐุง ูู ุทุฑููุฉ ุชุดุบูู ุงูุจูุช:**

1.) **ุงููุง, ุงุถููู ุงูู ูุฌููุนุชู.**
2.) **ุจุนุฏ ุฐุงูู, ูู ุจุชุฑููุชู ููุณุคูู.**
3.) **ุจุนุฏ ุฐุงูู ุงูุชุจ, .ุชุญุฏูุซ ูุชุญุฏูุซ ุงูุจูุงูุงุช.**
3.) **ุงุถู @{ASSISTANT_NAME} ูู ูุฌููุนุชู ุงู ุงูุชุจ .ุงูุถู **
4.) **ุจุนุฏ ุงููุงู ูู ุดู ูู ุจูุชุญ ูุญุงุฏุซุฉ ุตูุชูุฉ ูุงุณุชูุชุน.**
5.) **ุจุนุถ ุงูุงุญูุงู, ุณุชูุงุฌู ูุดุงูู ูู ุงูุชุดุบูู ูุงุนููู ููุท ุณูู ูุชุงุจุฉ ุงูุงูุฑ .ุชุญุฏูุซ**

๐ ** ุงุฐ ูู ููุถู ุญุณุงุจ ุงููุณุงุนุฏ ุงูุชุจ .ุงุทูุน , ูุจุนุฏ ุฐุงูู ุงูุชุจ .ุงูุถู**

๐ ** ุงู ูุดููุฉ ุชูุงุฌูุง ูุงุชุชุฑุฏุฏ ูู ุงูุชุญุฏุซ ูุน ุงููุทูุฑ: @T_M_X_0_0**

๐ __ุจูุงุณุทุฉ  {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ุฑุฌูุน", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ **ูุฑุญุจุง ุจู [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **ูุฑุญุจุง ุจู ูู ูุงุฆูุฉ ุงูุงูุงูุฑ ุงูุงุณุงุณูุฉ ููููู ูุนุฑูุฉ ุงูุงูุงูุฑ ุนู ุทุฑูู ุงุณุชุฎุฏุงู ุงูุงุฒุฑุงุฑ ุงุฏูุงุฉ !**

๐ __ุจูุงุณุทุฉ {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป ุงูุงูุฑ ุงููุดุฑููู", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป ุงูุงูุฑ ุงููุทูุฑ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ ุงูุงูุฑ ุงูุงุนุถุงุก", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ูุฑุญุจุง ุจู ูุฐุง ูู ุงูุงูุฑ ุงูุงุนุถุงุก:

ยป .ุดุบู - ูุชุดุบูู ุงุบููุฉ ุจุงูุฑุฏ ุนูู ููู ุตูุชู
ยป .ุชุฏูู - ูุชุดุบูู ุฑุงุฏูู ุจุซ ูุจุงุดุฑ
ยป .ููุฏูู - ุจุงูุฑุฏ ุนูู ููุทุน ููุฏูู
ยป .ูุจุงุดุฑ - ูุจุซ ูุจุงุดุฑ ูู ุงูููุชููุจ
ยป .ุงูุงูุชุถุงุฑ - ูุงุถูุงุฑ ูุงุฆูุฉ ุงูุงูุชุถุงุฑ
ยป .ุงุจุญุซูู - ูุชุญููู ููุฏูู ูู ุงูููุชููุจ
ยป .ุจุญุซ - ูุชุญููู ุงุบููุฉ ูู ุงูููุชููุจ
ยป .ูููุงุช - ูุงุถูุงุฑ ูููุงุช ุงุบููุฉ
ยป .ุฑุงุจุท - ูุงุถูุงุฑ ุฑุงุจุท ุงุบููุฉ

ยป .ุจูู - ุนุฑุถ ุญุงูุฉ ุงูุจูุช ุจููุบ
ยป .ูุญุต - ูุงุถูุงุฑ ุญุงูู ุงูุจูุช ุงู ูุนูู ุงู ูุง
ยป .ุงูุญุงูู - ูุญุต ุงูุจูุช ูู ุงููุฌููุนุฉ

๐ __ุจูุงุณุทุฉ {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ูุฑุญุจุง ุจู ูุฐุง ูู ุงูุงูุฑ ุงููุดุฑููู:

ยป .ุชููู - ูุงููุงู ุงูุงุบููุฉ ูุคูุชุง
ยป .ุงุณุชูุฑุงุฑ - ูุงุณุชูุฑุงุฑ ุงูุงุบููุฉ ุงููุชูููุฉ
ยป .ุชุฎุทู - ูุชุฎุทู ุงุบููุฉ , ููุฏูู
ยป .ุงููู - ูุงูุชูุงุก ุชุดุบูู ุงูููุณููู
ยป .ูุชู - ููุชู ุญุณุงุจ ุงููุณุงุนุฏ
ยป .ุงูุชุญ - ูุงูุบุงุก ูุชู ุญุณุงุจ ุงููุณุงุนุฏ
ยป .ุงุถุจุท `1-200` - ูุถุจุท ุญุฌู ุงูุตูุช
ยป .ุชุญุฏูุซ - ุงุนุงุฏุฉ ุชุดุบูู ูุชุญุฏูุซ ุจูุงูุงุช
ยป .ุงูุถู - ุฏุนูุฉ ุญุณุงุจ ุงููุณุงุนุฏ ูููุฌููุนุฉ
ยป .ุงุทูุน - ูุฎุฑูุฌ ุญุณุงุจ ูุณุงุนุฏ ูู ููุฌููุนุฉ

๐ __ุจูุงุณุทุฉ {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ูุฑุญุจุง ุจู ูุงูุทูุฑู ูู ุงูุงูุฑู ุงูุชุงููุฉ:

ยป .ุงูุณุญ - ุชูุธูู ุฌููุน ุงููููุงุช ุงูุฎุงู
ยป .ุญุฏุซ - ุชุญุฏูุซ ุงูุจูุช ุงูู ุงุฎุฑ ุงุตุฏุงุฑ
ยป .ุงููุธุงู - ุงุถูุงุฑ ูุนูููุงุช ุงููุธุงู
ยป .ุญุฏุซ - ูุชุญุฏูุซ ุงูุจูุช ุงูู ุงุญุฏุซ ุงุตุฏุงุฑ
ยป .ุงุนุงุฏุฉ - ุงุนุงุฏุฉ ุชุดุบูู ุงูุจูุช
ยป .ูุบุงุฏุฑุฉ ูู ุงููุฌููุนุงุช - ููุบุงุฏุฑุฉ ุญุณุงุจ ุงููุณุงุนุฏ ูู ูู ุงููุฌููุนุงุช

๐ __ุจูุงุณุทุฉ {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("ุงูุช ูุณุชุฎุฏู ูุญููู !\n\nยป ูุงุชุณุชุทูุน ุงุณุชุฎุฏุงู ุงูุจูุช.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐กูุฎุฑ ุงูุฏู ุงููุดุฑู ุงููุญูุฏ ุงูุฐู ูุฏูู ุตูุงุญูุฉ ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูููุฑ ุนูู ูุฐุง ุงูุฒุฑ !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **ุงุนุฏุงุฏุงุช ุงูุงุบููุฉ** {query.message.chat.title}\n\nโธ : ุงููุงู ูุคูุช\nโถ๏ธ : ุงุณุชูุฑุงุฑ\n๐ : ูุชู ุญุณุงุจ ุงููุณุงุนุฏ\n๐ : ุงูุบุงุก ูุชู ุญุณุงุจ ุงููุณุงุนุฏ\nโน : ุงููุงู ุงูุชุดุบูู",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("โน", callback_data="cbstop"),
                      InlineKeyboardButton("โธ", callback_data="cbpause"),
                      InlineKeyboardButton("โถ๏ธ", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("๐", callback_data="cbmute"),
                      InlineKeyboardButton("๐", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("๐ ุงุบูุงู", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("โ ูุงูู ุดู ูุดุชุบู ูุงุญูุงุฑ", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ูุฎุฑ ุงูุฏู ุงููุดุฑู ุงููุญูุฏ ุงูุฐู ูุฏูู ุตูุงุญูุฉ ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูููุฑ ุนูู ูุฐุง ุงูุฒุฑ !", show_alert=True)
    await query.message.delete()
