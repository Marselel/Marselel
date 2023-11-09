from aiogram import Dispatcher,Bot, executor,types
from random import choice

bot = Bot(token="6042247852:AAE7R_Acqe1UQe3KQOPur3IsAOD9PvXFBRA")
dp = Dispatcher(bot=bot)


def random_word():
    words = {"observant":"наблюдательный","obstinate":"упрямый","outgoing":"тусовщик","persitent":"настойчивый",
             "purposeful":"целеустремленный","quick witted":"находчивый","reserved":"cдержанный","respectful":"почтительный",
             "responsible":"ответственный","self-confident":"самоуверенный","self-possessed":"хладнокровный",
             "stable":"стабильный","tolerant":"терпимый","talkative":"розговорчивый","tough":"жесткий"}
    word = choice(list(words.keys()))
    return word,words[word]
class work:
    q = 0
    corr_ans = ""
@dp.message_handler()
async def start(mess: types.Message):
    a = mess.text
    if a=="/start":
        word,work.corr_ans=random_word()
        await mess.answer(f"Как переводится {word}")
        work.q = 1
    elif a=="Стоп":
        await mess.reply("Молодец! Пиши старт чтобы начать заново!")
        work.q = 00
    else:
        if work.q==1:
            if a.lower()==work.corr_ans:
                await mess.reply("Абсолютно верно!!!")
            else:
                await mess.reply(f"Неверно! Правильно - {work.corr_ans}")
            word,work.corr_ans=random_word()
            await mess.answer(f"Как переводится {word}")
executor.start_polling(dispatcher=dp,skip_updates=True)