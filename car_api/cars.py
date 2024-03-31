from fastapi import APIRouter

from database.carservice import get_cars, add_new_car,get_exact_users,get_exact_car,edit_car,delete_car
car_router = APIRouter(prefix='/car', tags=['Работа с машинами'])
# Получить все
@car_router.get('/all-cars')
async def all_cars():
    return await get_cars()
# Для добавления
@car_router.post('/add-car')
async def add_car(host_id: int,mark:str, model: str,name: str, status: str,cost : int, category: str):
    new_car_id = await add_new_car(host_id, mark,model,name,status,cost, category)
    return f'Успешно добавлен {new_car_id}'

# Получить пользователей кто
@car_router.get('/car-users')
async def get_user_cars(car_id: int):
    t_u = await get_exact_users(car_id)
    return  f'Успешно и вот данные {t_u}'
# Изменение определенногo car
@car_router.put('/edit')
async def edit_post(title_id:int,edit_info:str, new_info:str):
    result = edit_car(title_id,edit_info, new_info)
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка при изменении!'}
# Получить определенное car
@car_router.get('/get-car')
async def get_car(category: str):
    result = await get_exact_car(category)
    if result:
        return {'message': result}
    else:
        return {'message': 'Такое задание отсутствует!'}
# Запрос на удаление car
@car_router.delete('/delete_task')
async def delete_car(car_id: int):
    result = delete_car(car_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Такое задание отсутствует'}

