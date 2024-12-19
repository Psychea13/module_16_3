from fastapi import FastAPI, Path


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def root() -> str:
    return 'Главная страница'


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_users(username: str = Path(min_length=3, max_length=30),
                       age: int = Path(ge=1, le=120)) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_users(user_id: int, username: str = Path(min_length=3, max_length=30),
                       age: int = Path(ge=1, le=120)) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted.'


# uvicorn module_16_3:app --reload
