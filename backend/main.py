from urllib import response
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from database import update_todo_in_db, fetch_one_todo, fetch_all_todos, create_todo, delete_todo_in_db

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/get_all_todos')
async def get_all_todos():
    response =  await fetch_all_todos()
    return response


@app.get('/get_todo/{title}', response_model=Todo)
async def get_todo(title):
    response =  await fetch_one_todo(title)
    if response:
        return response
    raise  HTTPException(404, f"No todo item with title {title}")

@app.post('/post_todo', response_model=Todo)
async def post_todo(todo: Todo):
    response =  await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Error while creating todo")

@app.put('/update_todo/{title}', response_model=Todo)
async def update_todo(title: str, desc: str):
    response =  await update_todo_in_db(title, desc)
    if response:
        return response
    raise HTTPException(400, f"Error while updating todo {title}")


@app.delete('/delete_todo/{title}')
async def delete_todo(title):
    response =  await delete_todo_in_db(title)
    if response:
        return f"Successfully deleted todo- {title}"
    raise HTTPException(400, f"Error while deleting todo {title}")
