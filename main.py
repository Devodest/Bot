from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands

app = ApplicationBuilder().token("5636284208:AAEbIXEwY_wkXPL1aHnHWWlUmP1yotOXMGM").build()

app.add_handler(CommandHandler("Hi", bot_commands.hi_command))
app.add_handler(CommandHandler("time", bot_commands.time_command))
app.add_handler(CommandHandler("help", bot_commands.help_command))
app.add_handler(CommandHandler("sum", bot_commands.sum_command))
app.add_handler(CommandHandler("youtube", bot_commands.get_youtube))
app.add_handler(CommandHandler("weather", bot_commands.get_weather))


app.run_polling()