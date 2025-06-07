from apps.database.models import async_session, User
from sqlalchemy import select, delete
from sqlalchemy.exc import NoResultFound


async def set_user(data):
    async with async_session() as session:
        session.add(User(FIO = data["FIO"], number = data["number"],size = data["size"],  adress = data["address"]))
        await session.commit()


async def get_all_data():
    async with async_session() as session:
        users =  await session.scalars(select(User))
        text = ""
        i = 1
        for user in users:
            text += f"{i}. Имя: {user.FIO} || Номер: {user.number} || Размер:{user.size} || Адресс: {user.adress}\n"
            i+=1
        return text
    
    
    
async def delete_user(num: int):
    async with async_session() as session:
        user = await session.scalars(select(User))
        await session.scalar(delete(user))
        
        
async def delete_user(num: int):
    async with async_session() as session:
        try:
            result = await session.execute(
                select(User).offset(num - 1).limit(1)
            )
            user = result.scalar_one()
            await session.delete(user)
            await session.commit()
            return True
        except NoResultFound:
            return False 
        
        
