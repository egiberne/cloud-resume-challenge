# This file contains the main application code for the FastAPI backend. 
# It defines the API endpoints and handles the logic for counting user visits. 
# It also initializes the SQLite database


# Import the init_db function from database.py 
from .db_sqlite import init_db
# import the get_connection function from database.py
from .db_sqlite import get_connection

# Import system library to check 
import os
# Initialize DB only if it does not exist
if not os.path.exists("visits.db"):
    init_db()



## import fastapi library
from fastapi import FastAPI, Request
## import the CORS| Cross Origin Resource Sharing module
from fastapi.middleware.cors import CORSMiddleware


## create a fastapi instance 
app = FastAPI()


origins =['*']
methods =['*']
headers =['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

## GET requests

### create an endpoint at the root 
@app.get("/")
### define endpoint function  
def root():
### return message text
    return "Hello World, here is a Cloud Resumer Challenge by Emerick Giberne"

## create an endpoint health to check the health of the application
@app.get("/health")
### define endpoint function 
def health():
### return 
    return'"status":"ok"'

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
    

## POST Requests

### create an endpoint /echo to test the POST request
@app.post("/echo")
def echo():
    return '"received":"ok"'



## POST Request : create a endpoint /v1/visits to count the number of visits per user based on user id
### store number of visits per users based on user id
visit_counter={}
@app.post("/v1/visits")
async def set_counter(request:Request):
    data = await request.json()
    user_id=  data.get("userId")
    # check if userId is provided in the request
    if not user_id:
        return "userId is required"
    
    # Increment  visit count
    if user_id in visit_counter :
        visit_counter[user_id] += 1
    else : 
        visit_counter[user_id] = 1

    return { "userId": user_id, "visitCount": visit_counter[user_id] }

## create a endpoint /v2/visits to count the number of visits per user based on user id and store it in the SQLite database
@app.post("/v2/visits")
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



    