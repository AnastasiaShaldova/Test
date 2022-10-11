from app.pkg import db_connect
from app.pkg.models import User


async def user_add(user_details: User):
    """
    Функция добавляет пользователя в БД
    return: True or False
    """
    try:
        async with db_connect.connect() as conn:
            await conn.execute(
                "INSERT INTO public.users(user_name, gender) VALUES ($1, $2);",
                user_details.user_name, user_details.gender)
            return True
    except Exception:
        return False


async def get_user_by_name(user_name: str):
    """
    Функция ищет пользователя по имени
    name: имя пользователя
    return: None, если пользователь не найден
    return: {все данные}, если найден
    """
    async with db_connect.connect() as conn:
        users = await conn.fetchone(
            f"SELECT id, user_name, gender FROM public.users WHERE user_name = $1 ORDER BY user_name LIMIT 1",
            user_name)

        if users:
            return users[0]
        return None


async def users_get():
    """
    Функция выводит всех пользователей
    return: None, если пользователи не найдены
    return: [{"id": id, "login": login}, {...}, ...], если найдены
    """
    async with db_connect.connect() as conn:
        users = await conn.fetch(
            f"SELECT * FROM public.users")
        if users:
            return users
        return None




