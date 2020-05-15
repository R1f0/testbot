import telebot

from telebot import types

import COVID19Py
from telebot.apihelper import send_message

covid19 = COVID19Py.COVID19()

bot = telebot.TeleBot('1240677409:AAFf8jjN-O4oz2rOQ2cIoTka4j1qhvya73Q')



# Функция, что сработает при отправке команды Старт

# Здесь мы создаем быстрые кнопки, а также сообщение с привествием

@bot.message_handler(commands=['start'])

def start(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

	btn1 = types.KeyboardButton('Во всём мире')

	btn2 = types.KeyboardButton('Украина')

	btn3 = types.KeyboardButton('Россия')

	btn4 = types.KeyboardButton('Беларусь')

	btn5 = types.KeyboardButton('список добавленных стран')

	markup.add(btn1, btn2, btn3, btn4, btn5)



	send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса напишите " \

	f"название страны, например: США, Украина, Россия и так далее\n"

	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)



# Функция, что сработает при отправке какого-либо текста боту

# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране

@bot.message_handler(content_types=['text'])

def mess(message):

	# if message.text == 'список всех стран':
	# bot.send_message(message.chat.id, 'Добавленные страны:\nСША, Россия, Украина, Беларусь, Италия\n Испания, Китай, Бразилия, Польша, Япония\nГермания, Казахстан, Франция, Австралия\n')

	final_message = ""

	get_message_bot = message.text.strip().lower()

	if get_message_bot == "сша":

		location = covid19.getLocationByCountryCode("US")

	elif get_message_bot == "австралия":
		location = covid19.getLocationByCountryCode("AU")

	elif get_message_bot == "серевная корея":
		location = covid19.getLocationByCountryCode("KP")

	elif get_message_bot == "южная корея":
		location = covid19.getLocationByCountryCode("KR")

	elif get_message_bot == "индия":
		location = covid19.getLocationByCountryCode("IN")

	elif get_message_bot == "финляндия":
		location = covid19.getLocationByCountryCode("FI")

	elif get_message_bot == "норвегия":
		location = covid19.getLocationByCountryCode("NO")

	elif get_message_bot == "швеция":
		location =covid19.getLocationByCountryCode("SE")

	elif get_message_bot == "список добавленных стран":

		bot.send_message(message.chat.id,
						 'Добавленные страны:\nСША, Россия, Украина, Беларусь, Италия\n Испания, Китай, Бразилия, Польша, Япония'
						 '\nГермания, Казахстан, Франция, Австралия, северная корея\nюжная корея, индия, финляндия, норвегия, ')

		location = covid19.getLatest()
		final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

	elif get_message_bot == "украина":

		location = covid19.getLocationByCountryCode("UA")

	elif get_message_bot == "россия":

		location = covid19.getLocationByCountryCode("RU")

	elif get_message_bot == "беларусь":

		location = covid19.getLocationByCountryCode("BY")

	elif get_message_bot == "казакхстан":

		location = covid19.getLocationByCountryCode("KZ")

	elif get_message_bot == "италия":

		location = covid19.getLocationByCountryCode("IT")

	elif get_message_bot == "франция":

		location = covid19.getLocationByCountryCode("FR")

	elif get_message_bot == "германия":

		location = covid19.getLocationByCountryCode("DE")

	elif get_message_bot == "япония":

		location = covid19.getLocationByCountryCode("JP")

	elif get_message_bot == "испания":

		location = covid19.getLocationByCountryCode("ES")

	elif get_message_bot == "польша":

		location = covid19.getLocationByCountryCode("PL")

	elif get_message_bot == "бразилия":

		location = covid19.getLocationByCountryCode("BR")

	elif get_message_bot == "китай":

		location = covid19.getLocationByCountryCode("CN")

	else:

		location = covid19.getLatest()

		final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"



	if final_message == "":

		date = location[0]['last_updated'].split("T")

		time = date[1].split(".")

		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
			 f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
			 f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
			 f"{location[0]['latest']['deaths']:,}"



	bot.send_message(message.chat.id, final_message, parse_mode='html')



# Это нужно чтобы бот работал всё время

bot.polling(none_stop=True)
