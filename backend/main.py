# Runing: fastapi dev main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ai-chat-ap"}

# POST: to create data
# GET: to read data
# PUT: to update data
# DELETE: to delete data

# /home
# /chat
# /chat/response
# /chat/text
# /history






