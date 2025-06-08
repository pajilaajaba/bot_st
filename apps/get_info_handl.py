from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import os
from dotenv import load_dotenv

import apps.keyboard as kb
from apps.states import Person, Key
import apps.database.request as rq

router = Router()

@router.message(CommandStart())
async def start_handle(message: Message):
    await message.answer("Привет, выбери одну из предложенных ф-ций внизу👀⬇️", 
                         reply_markup=kb.start_mess)
    
    
@router.callback_query(F.data == 'supp')
async def supp_handle(callback: CallbackQuery):
    await callback.message.edit_text("Вот создатель ➡️➡️➡️ к нему все вопросы @Stequa", reply_markup = kb.back)
    
    
@router.callback_query(F.data == 'back')
async def back_to_menu(callback: CallbackQuery):
    await callback. message.edit_text("Привет, выбери одну из предложенных ф-ций внизу👀⬇️", 
                         reply_markup=kb.start_mess)
    
    
@router.callback_query(F.data == 'longsliv')
async def begin_input(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите имя")
    await state.clear()
    await state.set_state(Person.FIO)
    
    
@router.message(Person.FIO)
async def FIO_input(message: Message, state: FSMContext):
    await state.update_data(FIO = message.text)
    await state.set_state(Person.number)
    await message.answer("Введите номер телефона")
    
@router.message(Person.number)
async def number_input(message: Message, state: FSMContext):
    await state.update_data(number = message.text)
    await state.set_state(None)
    await message.answer("Введите размер лонгслива", reply_markup=kb.size)
    
@router.callback_query((F.data == 'l') | (F.data == 'm') | (F.data == 'xl'))
async def size_input(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    tex = callback.data.upper()
    await state.set_state(Person.size)
    await state.update_data(size = tex)
    await state.set_state(Person.address)
    await callback.message.delete()
    await callback.message.answer("Введите адресс доставки")
    
    
    
@router.message(Person.address)
async def adress_input(message: Message, state: FSMContext):
    await state.update_data(address = message.text)
    data = await state.get_data()
    await state.set_state(None)
    await message.answer(f"Вы ввели\nФИО: {data["FIO"]}\nНомер: {data["number"]}\nРазмер: {data['size']}\nАдресс: {data["address"]}",
                         reply_markup=kb.check_correct)
    
    
    

    
@router.callback_query(F.data == 'correct')
async def correct_handle(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.edit_text(f"Вы ввели\nФИО: {data["FIO"]}\nНомер: {data["number"]}\nРазмер: {data['size']}\nАдресс: {data["address"]}")
    await callback.answer()
    await rq.set_user(data)
    await state.clear()
    await callback.message.answer("Данные успешно введены, с вами свяжутся для потверждения", reply_markup=kb.back)
    
    
    
    
    
@router.message(F.text == "/admin")
async def admin_allow(message: Message, state: FSMContext):
    await message.answer("Введите ключ доступа")
    await state.clear()
    await state.set_state(Key.key)
    
    
@router.message(Key.key)
async def admin_outp(message: Message, state: FSMContext):
    tex = message.text
    await state.clear()
    load_dotenv()
    password = os.getenv("Password")
    if (tex == password):
        await message.answer("Выберите команду ниже", reply_markup=kb.admin)
        
        
@router.callback_query(F.data == 'outp_list')
async def correct_handle(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(await rq.get_all_data(), reply_markup=kb.close)
        
        
@router.callback_query(F.data == 'clos')
async def correct_handle(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выберите команду ниже", reply_markup=kb.admin)
    
    
    
@router.callback_query(F.data == 'del_user')
async def correct_handle(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text("Введите номер пользователья для удаления")
    await state.set_state(Key.num)
    
    
@router.message(Key.num)
async def adress_input(message: Message, state: FSMContext):
    try:
        tex = int(message.text)
    except ValueError:
        await message.answer("Даун ебаный ЧИСЛО")
        return
    success = await rq.delete_user(tex)
    if success:
        await state.clear()
        await message.answer("Удаление успешно", reply_markup=kb.close)
    else:
        await state.clear()
        await message.answer("Пользователь не найден", reply_markup=kb.close)