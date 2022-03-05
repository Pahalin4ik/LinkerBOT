import logging
from aiogram import Bot, Dispatcher, executor, types, utils

#state
from Link import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOCKEN = "5193701375:AAE6x3jZ-r9bT5P9gA8IlmcmaDMYCmIMvIY"
bot = Bot(token=TOCKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# @dp.message_handler()
# async def link_Echom(message: types.Message):
#     await message.reply(Link.getLink(message.text, "https://www.google.com/"))

@dp.message_handler(commands=['link', 'l'], state=None)
async def Start(message: types.message):
    await Link.link.set()
    await message.reply("Please send link")

@dp.message_handler(state=Link.link)
async def GetLink(message: types.message, state: FSMContext):
    if not Link.getLink(message.text) == None:
        async with state.proxy() as data:
            data['link'] = Link.getLink(message.text)
        await Link.text.set()
        await message.reply("Please send text")
    else:
        await message.reply("It doesn't link or link doesn't valid")

@dp.message_handler(state=Link.text)
async def GetText(message: types.message, state: FSMContext):
    link = ''
    async with state.proxy() as data:
        link = data['link']
    await message.reply(Link.getTagLink(message.text, link))
    await message.answer('Bot created by <a href="https://www.youtube.com/channel/UCzCmbETDe3Xd_pLylD9-ciQ">Pahalin4ik</a>')
    await state.finish()

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
