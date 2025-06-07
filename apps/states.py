from aiogram.fsm.state import StatesGroup, State

class Person(StatesGroup):
    FIO = State()
    number = State()
    address = State()
    size = State()
    
    
class Key(StatesGroup):
    key = State()
    num = State()