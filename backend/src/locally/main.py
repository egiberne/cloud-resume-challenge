# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the init_db function from module db_sqlite.py 
from backend.src.locally.db_sqlite import init_db
# import the get_connection function from db_sqlite.py 
from backend.src.locally.db_sqlite import get_connection

# Import system library to check 
import os

# Initialize DB only if it does not exist
if not os.path.exists("database/visits.db"):
    init_db()


app = FastAPI()



origins =['*']
methods =['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_method=methods,
    allow_headers=['*'],
)

## GET REQUESTS
@app.get("/")
def read_root():
    return {"Hello": "World"}



## create an endpoint /v2/visits to get the number of visits per user based on user id and get it from the SQLite database
@app.get("/v2/visits")
async def get_counter(userId: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT visitCount, dbID FROM visits WHERE userId = ?", (userId,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"dbID": row["dbID"], "userId": userId, "visitCount": row["visitCount"]}
    else:
        return {"dbID": None, "userId": userId, "visitCount": 0}
    

## POST REQUESTS

## create a endpoint /v2/visits to count the number of visits per user based on user id and store it in the SQLite database
@app.post("/v2/visit")
async def set_counter(request: Request):
    data = await request.json()
    user_id = data.get("userId")

    if not user_id:
        return {"error": "userId is required"}

    conn = get_connection()
    cursor = conn.cursor()

    # 1. Check if user exists
    cursor.execute("SELECT visitCount FROM visits WHERE userId = ?", (user_id,))
    row = cursor.fetchone()

    # 2. Increment or initialize
    if row:
        new_count = row["visitCount"] + 1
        cursor.execute(
            "UPDATE visits SET visitCount = ? WHERE userId = ?",
            (new_count, user_id)
        )
    else:
        new_count = 1
        db_id = None
        cursor.execute(
            "INSERT INTO visits (dbId, userId, visitCount) VALUES (?, ?, ?)",
            (db_id, user_id, new_count)
        )


    cursor.execute("SELECT dbId FROM visits WHERE userId = ?", (user_id,))
    db_id = cursor.fetchone()["dbID"]
    conn.commit()
    conn.close()


    return {"dbID": db_id, "userId": user_id, "visitCount": new_count}