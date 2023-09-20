from aiogram import types
from random import randint
from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup, Message
import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver import ActionChains
import os
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from bs4 import BeautifulSoup as bs
from collections.abc import Mapping
from rps_inference import neural
import pytesseract
from PIL import Image
import os
import openai


def prazdnik():
    link = 'https://kakoysegodnyaprazdnik.ru/'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

    response = requests.get(url=link, headers=HEADERS)
    soup = bs(response.content, 'html.parser')
    block = soup.find('div', class_='listing_wr')
    cards = block.findAll('div', itemprop='suggestedAnswer')
    # for item in cards:
    #     name=item.find('span',itemprop='text').text
    #     print(name)
    # break
    nazvaniya = [item.find('span', itemprop='text').text for item in cards][0:10]
    return '\n'.join( nazvaniya)



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

bot = Bot(token='6062302036:AAH7LpXx6jotQenO5PJ8nbB15TqWqvQjKl0')
dp = Dispatcher(bot=bot)


class work:
    q = 0
    markback = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Назад⬅️'))
    markstart = ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = KeyboardButton('Рандомное число🎲')
    i2 = KeyboardButton('Погода⛱')
    i3= KeyboardButton('Текст песни📄')
    i4=KeyboardButton('Калькулятор*️⃣')
    i5=KeyboardButton('Какой сегодня праздник🥳')
    i6=KeyboardButton('Мои оценки🔢')
    i7=KeyboardButton('ЧатGPT')
    i8=KeyboardButton('ИИ🧠')
    markstart.add(i1).add(i2,i3).add(i4,i7).add(i8)
    data = {}
    loc = ''
    place=''
    prazdnik=''
    k=0
    w = ['сегодня', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

async def on_start(_):
    print('tg6_bot.py вышел в онлайн!')

def dollar():
    site='https://www.google.com/search?q=dollar'
    page=requests.get(site,headers=HEADERS)
    soup=BeautifulSoup(page.content,'html.parser')
    convert=soup.findAll('span',{'class':'DFlfde SwHCTb'})
    print(convert[0].text)
def randomi(x):
    try:
        w = [int(i) for i in x.split()]
        return f'Ваше рандомное число: {randint(min(w), max(w))}'
    except:
        return 'Впишите два числа'


def text(x):
        a = ''
        site = f'https://www.google.com/search?q={"+".join(x.split())}+lyrics&oq=+&aqs=chrome.0.69i59j69i57j0i512j46i131i340i433i512l2j0i512l5.4575j0j15&sourceid=chrome&ie=UTF-8'
        page = requests.get(site, headers=HEADERS)
        soup = BeautifulSoup(page.content, 'html.parser')
        convert = soup.findAll('span', {'jsname': 'YS01Ge'})
        namesong = soup.findAll('span', {'role': 'heading'})
        songer = soup.findAll('div', {'class': 'wx62f PZPZlf x7XAkb'})
        if len(songer) != 0:
            a += songer[0].text[7:] + ' — ' + namesong[0].text + '\n' + '\n'
        for i in convert:
            a = a + i.text + '\n'
        if len(a) == 0:
            site = f'https://www.google.com/search?q={"+".join(x.split())}+lyrics'
            mainpage = requests.get(site, headers=HEADERS)
            soup1 = BeautifulSoup(mainpage.content, 'html.parser')
            site = soup1.find('span', class_='dyjrff qzEoUe').text[3:]
            if site != 'song':
                return f'Извините я не нашел такую песню в гугле, но вот ссылка на сайт с текстом: \n https://genius.com/{site}'
            return 'Введите песню а не набор букв'
        return a



def yaweather(loc):
    link = f'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+{loc}'
    responce = requests.get(url=link, headers=HEADERS)
    soup = BeautifulSoup(responce.content, 'html.parser')
    try:
        block = soup.find('div', class_='wob_dfc')
        cards = block.find_all('div', class_='wob_df')
        k = 0
        DATA = dict()
        for item in cards:
            facts = item.find('img', class_='YQ4gaf zr758c').get('alt')
            temp = str(item.find('span', class_='wob_t').text) + '°C'
            if k != 0:
                day = item.find('div', class_='Z1VzSb').get('aria-label')
            else:
                day = 'сегодня'
            k += 1
            DATA[day] = temp
            work.data = DATA
            work.place=soup.find('span',class_='BBwThe').text
    except:
        return 'не нашлось такого места'


def yaweather2(loc, dayl):
    link = f'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+{loc}'
    responce = requests.get(url=link, headers=HEADERS)
    soup = BeautifulSoup(responce.content, 'html.parser')
    try:
        block = soup.find('div', class_='wob_dfc')
        cards = block.find_all('div', class_='wob_df')
        k = 0
        DATA = dict()
        for item in cards:
            facts = item.find('img', class_='YQ4gaf zr758c').get('alt')
            temp = str(item.find('span', class_='wob_t').text) + '°C'
            if k != 0:
                day = item.find('div', class_='Z1VzSb').get('aria-label')
            else:
                day = 'сегодня'
            k += 1
            DATA[day] = temp+' ('+facts+')'
            work.data = DATA
        return DATA[dayl]
    except:
        return 'не нашлось такого места'
#
def prazdnik1(number):
    responce=requests.get(url='https://kakoysegodnyaprazdnik.ru/')
def remove_file(name):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), name)
    os.remove(path)
def konspekt(path,phrase) -> str:

    img = Image.open(path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'

    text = pytesseract.image_to_string(img, lang='rus',config=tessdata_dir_config)
    # print(text)
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{phrase}:\n{text}"}
        ]
    )

    return str(completion.choices[0].message.content)


# def marks():
#     driver = webdriver.Chrome()
#     driver.get(url='https://elschool.ru/Logon/Index')
#     driver.maximize_window()
#     username_input = driver.find_element(By.CLASS_NAME, 'form-control')
#     username_input.send_keys('ИстяковММ')
#     password_input = driver.find_element(By.ID, 'password').send_keys('111111aA')
#     button = driver.find_element(By.XPATH, '//button[@type="button"]').click()
#     sleep(2)
#     dnevnik = driver.find_element(By.XPATH, '//a[@role="button"]').click()
#     sleep(2)
#     tabel = driver.find_element(By.PARTIAL_LINK_TEXT, 'Табель').click()
#     sleep(3)
#     driver.get_screenshot_as_file(fr'C:\Users\user\Pictures\Папка для фоток для тг бота\{work.k}.png')
#     work.k += 1
#     sleep(3)
#     ActionChains(driver).scroll_from_origin(ScrollOrigin.from_viewport(10, 10), 0, 600).perform()
#     sleep(0.5)
#     driver.get_screenshot_as_file(fr'C:\Users\user\Pictures\Папка для фоток для тг бота\{work.k}.png')
#     sleep(0.5)
#     driver.close()
#     driver.quit()
# marks()



@dp.message_handler(commands='start')
async def start(mess: Message):
    await mess.answer(f'Привет, я умею выполнять различные функции, выбери какую нибудь!', reply_markup=work.markstart)

'''**********************************************************************************************************************************************************************************************************
****************************************************************************************************************************************************************************************************************
*****************************************************************************************************************************************************************************************************'''

@dp.message_handler(content_types=['text'])
async def all_messages(mess: Message):
    a = mess.text
    if a == 'Рандомное число🎲':
        work.q = 1
        await mess.answer('Впишите два числа', reply_markup=work.markback)
    elif a == 'Назад⬅️':
        work.q = 0
        await  mess.answer('Вы вернулись в главное меню!', reply_markup=work.markstart)
    elif a == 'Погода⛱':
        work.q = 2
        await mess.answer('Введите место для определения температуры в нем', reply_markup=work.markback)
    elif a=='Текст песни📄':
        work.q=3
        await mess.reply('Введите название песни',reply_markup=work.markback)
    elif a=='Калькулятор*️⃣':
        work.q=4
        await mess.answer('Впишите пример',reply_markup=work.markback)
    elif a=='Мои оценки🔢':
        await bot.send_photo(mess.from_user.id,open(fr'C:\Users\user\Pictures\Папка для фоток для тг бота\{work.k-1}.png','rb'))
        await bot.send_photo(mess.from_user.id,open(fr'C:\Users\user\Pictures\Папка для фоток для тг бота\{(work.k)}.png','rb'))
        # remove_file(fr'C:\Users\user\Pictures\Папка для фоток для тг бота\{(work.k)}.png')
        # remove_file(fr'C:\Users\user\Pictures\Папка для фоток для тг бота\{(work.k-1)}.png')
    elif a=='Какой сегодня праздник🥳':
        await mess.answer(f'Сегодня празднуются {prazdnik()}')
    elif a=='ЧатGPT':
        work.q=5
        await mess.answer("Привет скинь мне фотку для конспекта!",reply_markup=work.markback)
    elif a=='ИИ🧠':
        work.q=6
        await mess.answer('Привет, отправь мне фотку руки в положении "камень", "ножницы" или "бумаги" и я отгадаю что на фотке',reply_markup=work.markback)
    else:
        if work.q == 1:
            await mess.answer(randomi(a))
        elif work.q == 2:
            if yaweather(a) != 'не нашлось такого места':
                yaweather(a)
                w = [i for i in work.data]
                inkb = InlineKeyboardMarkup()
                d1 = InlineKeyboardButton(text=w[0], callback_data=w[0])
                d2 = InlineKeyboardButton(text=w[1], callback_data=w[1])
                d3 = InlineKeyboardButton(text=w[2], callback_data=w[2])
                d4 = InlineKeyboardButton(text=w[3], callback_data=w[3])
                d5 = InlineKeyboardButton(text=w[4], callback_data=w[4])
                d6 = InlineKeyboardButton(text=w[5], callback_data=w[5])
                d7 = InlineKeyboardButton(text=w[6], callback_data=w[6])
                d8 = InlineKeyboardButton(text=w[7], callback_data=w[7])
                inkb.add(d1, d2, d3, d4, d5, d6, d7, d8)
                await mess.answer(f'Выберите день недели для просмотра погоды в "{work.place}"', reply_markup=inkb)
                work.loc = a
                q = 0

            else:
                await  mess.reply('Не нашлось такого места')
        elif work.q==3:
            await mess.reply(text(a))
        elif work.q==4:
            await mess.answer(eval(a.replace('^','**')))
        elif work.q==5:
            await mess.answer('Скинь фоткуууу')
        elif work.q==11:
            try:
                await mess.answer("Ждите, я генерирую ответ")
                await  mess.answer(konspekt('images/hello.jpg',a))
                # remove_file("images/hello.jpg")
            except Exception as ex:
                await mess.reply("Что то пошло не так")


        else:
            await mess.reply('Выбери команду')
    print(mess.chat.first_name,mess.text)

@dp.message_handler(content_types=['photo'])
async def raspoznatel(mess: Message):
    if work.q==6:

        await mess.photo[-1].download('images/image.jpg')
        await mess.answer("Фото загружено!")
        await mess.answer(neural('images/image.jpg'))
        # remove_file('images/image.jpg')
    elif work.q==5:
        await mess.photo[-1].download('images/hello.jpg')
        await mess.reply("Фотография успешно загружена!")
        work.q=11
        await mess.answer("Теперь введите что сделать с этим текстом для ChatGPT",reply_markup=work.markback)
@dp.callback_query_handler()
async def call_back(callback: types.CallbackQuery):
    await callback.message.answer(f'В {callback.data} будет {yaweather2(work.loc, callback.data)}')
    await callback.answer()
    print(callback.data)

# @dp.callback_query_handler()
# async def numbers(callback:types.CallbackQuery):
#     await callback.message.answer(prazdnik1(callback.data))
#     await  callback.answer()

executor.start_polling(dp, skip_updates=True, on_startup=on_start)
