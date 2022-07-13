from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Botu Qrupa Əlavə Et", url=f"http://t.me/LacosteGameAzBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("Yeniliklər 🔔", url="https://t.me/LacosteGameResmi"),
        InlineKeyboardButton("Sahib 🌐", url="https://t.me/Axhmedov"),
    ]
])


START = """
**• Salam 🇦🇿

• Mən Qruplar üçün hazırlanmış oyun Botuyam 🇦🇿 

• Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən ✍🏻 

• 🌐 Bot @Axhmedov Tərəfindən Yaradılmışdır.

➤ Məlumat üçün 👉 /help bas. Komandalar Asand və Rahatdır. 
"""

HELP = """
**⌨️ Əmrlər  Menyusuna Xoşgəldin.📌**
/basla - Oyunu başlatmaq üçün
/pass - Üç dəfə işlədə bilərsiz, oyunu keçmək üçün
/reyting - Global reytinq
/dayandir - Oyunda çıxmaq üçün lazım olan əmr
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyun")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Qrupunuzda Artıq Davam Edir ✍🏻 \n Oyunu dayandırmaq üçün yazın /dayandir")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nKəlimə Tapma Oyunu Başladı .\n\nBol Şanslar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazanacağınız Xal: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən düzgün sözü tapın
        """
        await c.send_message(m.chat.id, text)
        
