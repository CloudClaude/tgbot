from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from app.keyboards import main
from random import randint

bot = Bot(token = '7299361034:AAGOekebelrRoXoWRXn9bRq36_ND0EtJtaU')

router = Router()

imglist =[]

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(text = f"Здравствуйте, {message.from_user.full_name}.", reply_markup=main)

@router.message(F.text == 'Информация')
async def about(message: types.message):
    await message.answer(text="Данный бот предоставляет мотивационную картинку по нажатию кнопки.")

@router.message(F.text == 'Мотивационная картинка')
async def send(message: types.Message):
 
    image_url = imglist[randint(0, len(imglist)-1)]
    await bot.send_photo(message.chat.id, str(image_url))

def imageslist(x):
    imglist.append(x)
    if imglist != []:
        print(imglist)
    else:
        print('Empty')