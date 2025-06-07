from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_mess = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'Заказать ЛОНГСЛИВ', callback_data = 'longsliv'), 
                                                    InlineKeyboardButton(text = 'Поддержка', callback_data = 'supp')]])

back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'назад', callback_data = 'back')]])


check_correct = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'Все верно', callback_data = 'correct'), 
                                                    InlineKeyboardButton(text = 'Ввести заново', callback_data = 'longsliv')]])

size = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'M', callback_data = 'm'), 
                                                    InlineKeyboardButton(text = 'L', callback_data = 'l'), 
                                                    InlineKeyboardButton(text = 'XL', callback_data = 'xl')]])

admin = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'Вывести список', callback_data = 'outp_list'), 
                                                    InlineKeyboardButton(text = 'Удалить пользователя', callback_data = 'del_user')]])

close = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = 'закрыть', callback_data = 'clos')]])
