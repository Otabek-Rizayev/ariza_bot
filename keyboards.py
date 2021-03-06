from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import loader
from pathlib import Path
from main import dp, bot, _
from lang import LANGS, LANG_STORAGE, Localization

btnMain = KeyboardButton(_("๐ Orqaga"))
Main = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)


feed = KeyboardButton(_("๐ฌ Adminga xabar qoldirish"))
ar = KeyboardButton(_("๐ Ariza qoldirish"))
biz = KeyboardButton(_("๐ค Biz haqimizda"))
ch = KeyboardButton("๐บ๐ฟUZ|๐ท๐บRU|๐ฌ๐งENG")
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(feed, ar).add(biz, ch)

ex = KeyboardButton(_("Meneger"))
kur = KeyboardButton(_("Buxgalter"))
biz = KeyboardButton(_("Injiner"))
yur = KeyboardButton(_("Loyiha boshqaruvchisi"))
ish = ReplyKeyboardMarkup(resize_keyboard=True).add(ex, kur).add(biz, yur).add(btnMain)

uz = InlineKeyboardButton(text="๐บ๐ฟ O'zbekcha", callback_data="๐บ๐ฟ O'zbekcha")
ru = InlineKeyboardButton(text="๐ท๐บ ะ ัััะบะธะน", callback_data="๐ท๐บ ะ ัััะบะธะน")
eng = InlineKeyboardButton(text="๐ฌ๐ง English", callback_data="๐ฌ๐ง English")
til = InlineKeyboardMarkup(row_width=3).add(uz, ru, eng)
