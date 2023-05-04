import telebot
from telebot import types

bot = telebot.TeleBot("6254770483:AAECU4Ul81PjRHqq7xUCY36wpKbVObCVXyo")

keyboard = types.ReplyKeyboardMarkup(row_width=1)
button1 = types.KeyboardButton('Html')
button2 = types.KeyboardButton('Python')
button3 = types.KeyboardButton('Web Design')
button4 = types.KeyboardButton('LightRoom')
button5 = types.KeyboardButton('After Effects')
button6 = types.KeyboardButton('Swagger Tools')
button7 = types.KeyboardButton('Cloud Computing')
button8 = types.KeyboardButton('Cloud Security')
button9 = types.KeyboardButton('Coding Basics')

keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱ \n▱ Hi! This is Udemy Course Provider... ▱ \n▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱ \n \n Type '/help' for more... \n\n\n\n Udemy Course Provider | ℂ𝕪𝕓𝕖𝕣 𝕊𝕙𝕒𝕣𝕖 『🇱🇰』 ")
    bot.reply_to(message, " You must JOIN this Channel. All the upadtes & bugs send to this channel ⚠️ \n  \n https://t.me/udemy_course_provider ")

@bot.message_handler(commands=['refresh'])
def start(message):
    bot.reply_to(message, "Bot refreshed successful... ")

@bot.message_handler(commands=['help'])
def start(message):
    bot.reply_to(message, "All the commands are HERE 👇👇 \n \n     /restart - to restart the bot \n     /help - to get help \n     /courses- to get all the courses \n     /channel - to join the channel \n\n\n  be enjoy... : )")

@bot.message_handler(commands=['courses'])
def start(message):
    bot.send_message(message.chat.id, 'Here are the all courses... Enroll all for free', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Html':
        bot.send_message(message.chat.id, ' Here is a best HTML course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/41z8vVY  \n \n Happy Learning... ; ) ')

    elif message.text == 'Python':
        bot.send_message(message.chat.id, ' Here is a best PYTHON course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/3MWgh8n  \n \n Happy Learning... ; ) ')

    elif message.text == 'Web Design':
        bot.send_message(message.chat.id, ' Here is a best Web Designing course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/40X9G0A  \n \n Happy Learning... ; ) ')

    elif message.text == 'LightRoom':
        bot.send_message(message.chat.id, ' Here is a best Lightroom Photo Editing course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/41RP7UG  \n \n Happy Learning... ; ) ')

    elif message.text == 'After Effects':
        bot.send_message(message.chat.id, ' Here is a best Adobe After Effects course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/3ALMurB  \n \n Happy Learning... ; ) ')

    elif message.text == 'Swagger Tools':
        bot.send_message(message.chat.id, ' Here is a best Swagger Tools course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/3Lt4AU8  \n \n Happy Learning... ; ) ')

    elif message.text == 'Cloud Computing':
        bot.send_message(message.chat.id, ' Here is a best Cloud Computing course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/3nquYGj  \n \n Happy Learning... ; ) ')

    elif message.text == 'Cloud Security':
        bot.send_message(message.chat.id, ' Here is a best Cloud Security course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/3NtdWlz  \n \n Happy Learning... ; ) ')

    elif message.text == 'Coding Basics':
        bot.send_message(message.chat.id, ' Here is a best Coding Basics course by Udemy... Enroll the course free for life time ; ) \n \n  https://bit.ly/3nwqIoF  \n \n Happy Learning... ; ) ')


@bot.message_handler(commands=['channel'])
def start(message):
    bot.reply_to(message, "හෙලෝ කස්ටිය...😊 \n \n ඔන්න අපි ඉතිම් අලුත් චැනල් එකක් හැදුවා….💫 \n 🤩 ඉතිම් ඕගොල්ලන්ට මේකෙන් 😊 ,\n \n             ⭕️Programing \n             ⭕️Coding \n             ⭕️Ethical hacking \n             ⭕️Tech News \n             ⭕️Tutorials \n             ⭕️Tips & Tricks \n \n         💢වගේ හුගක් දේවල් ඉගෙන ගන්න පුලුවන්...☺️ \n\n👨‍💻ලගදී පටන් ගත්තෙ.. ඒක නිසා කස්ටියම Join වෙලා බලම්න.. පහළ තියෙන links click කරල join වෙම්න..❤️‍🔥 \n\n         Channel 😊 - @Cyber_Share  ✅ \n         Discussion ❤️ - @CyberShare_discussion  ✅ \n         owner 🔰 -  @cybershare_bot  ✅ \n \n       🚫 Disclaimer 🚫 \n We do not promote any illegal or violent content. \n \n \n Copyrights ©️ 2023 ℂ𝕪𝕓𝕖𝕣 𝕊𝕙𝕒𝕣𝕖 ❤️")


@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text.lower() == "hi":
        bot.reply_to(message, "Bye !")
    if message.text.lower() == "bye":
        bot.reply_to(message, "Hi !")
    else:
        bot.reply_to(message, "Idk" )

bot.polling()
