import datetime
import requests
from spy import *
from data_base import path_youtube, open_weather_token
from pytube import YouTube


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'/Hi\n/time\n/help\n/sum - сумма двух чисел\n/you - информация о видео YouTube\n'
                                    f'/weather <название города>')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x + y}')


async def get_youtube(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    vid = YouTube(path_youtube)
    await update.message.reply_text(f'Title: {vid.title}\nViews: {vid.views}')


async def start_weather_commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Привет, напиши название города, а я пришлю сводку погоды')


async def get_weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    city = update.message.text.split()
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city[1]}&appid={open_weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        await update.message.reply_text(f'Погодова в городе: {city}\nТемпература: {cur_weather}\n'
                                        f'влажность: {humidity}\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n'
                                        f'Хорошего дня!'
                                        )
    except:
        await update.message.reply_text('Проверьте название города')
