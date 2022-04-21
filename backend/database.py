from model import Todo
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.TodoList
collection = database.todo


async def update_todo_in_db(title, desc):
    await collection.update_one({"title": title}, {"$set": { "description": desc }})
    return await collection.find_one({"title": title})

 
async def delete_todo_in_db(title):
    await collection.delete_one({"title": title})
    return True

async def fetch_one_todo(title):
    return await collection.find_one({"title": title})
 

async def fetch_all_todos():
   return [Todo(**document) async for document in collection.find({})]


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document



