from database.models import Car
from database import get_db
# Добавление
async def add_new_car(host_id,mark, model, status, name, category,cost):
    db = next(get_db())
    new_car = Car(host_id=host_id, mark=mark, model=model, status=status,
                    category=category,name=name,cost=cost)
    db.add(new_car)
    db.commit()
    return new_car.car_id
# Получить все
async def get_cars():
    db = next(get_db())
    cars = db.query(Car).all()
    return cars
# Получить определенное
async def get_exact_car(category):
    db = next(get_db())
    tasks = db.query(Car).filter_by(category=category).all()

    if tasks:
        task_titles = [task.name for task in tasks]
        return ', '.join(task_titles)
    else:
        return 'Ничего не найдено'


#  Удаление
def delete_car(car_id):
    db = next(get_db())
    car = db.query(Car).filter_by(car_id=car_id).first()
    if car:
        db.delete(car)
        db.commit()
        return f' {car_id} удален'
    else:
        return 'Задание не найдено'
# Изменение
def edit_car(car_id, edit_info, new_info):
    db = next(get_db())
    exact_task = db.query(Car).filter_by(car_id=car_id).first()
    if exact_task:
        if edit_info == 'mark':
            exact_task.mark = new_info
        elif edit_info == 'model':
            exact_task.model = new_info
        elif edit_info == 'cost':
            exact_task.cost = new_info
        elif edit_info == 'category':
            exact_task.category = new_info
        if edit_info == 'user_id':
            if exact_task.user_id is None:
                exact_task.user_id = new_info
            else:
                 # If a user already exists, update the user_id
                if new_info not in exact_task.user_id:
                    exact_task.user_id += ',' + new_info
        db.commit()  # Сохраняем изменения в базе данных

        return 'успешно изменено!'
    else:
        return 'не найдено'

async def get_exact_users(car_id):
    db = next(get_db())
    checker = db.query(Car).filter_by(car_id=car_id).all()
    if checker:
        users_id = [str(users.user_id) for users in checker if users.user_id is not None]
        return ', '.join(users_id)
    else:
        return 'Ничего не найдено'

