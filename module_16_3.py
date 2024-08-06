from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_all_user() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    user_id = int(max(users.keys(), key=lambda k: users[k])) + 1
    users[user_id] = f"Имя: {username}, возраст: {age}"
    
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    
    return f"User {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
