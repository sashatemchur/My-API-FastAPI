from typing import Union
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()
api = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=clients"
output = requests.get(api)
output = output.json()

with open("data.json", "r", encoding="UTF-8") as data: 
    data_read = json.load(data)
    
    
def output_file_api():
    # This function writes data from API to a json file
    with open("data.json", "w", encoding="UTF-8") as data: 
        json.dump(output, data, indent=4)
    

@app.get("/")
def read_root():
    # This function outputs the data from the second API to our API 
    return data_read


@app.get("/user_id/{id}")
def read_item(id: str):
    # This function displays the user by the specified ID that we specified in the search flow
    for i in range(len(data_read)):
        if id == data_read[i]["id"]: 
            return data_read[i]


@app.put("/user_balance/{id}/{balance}")
def update_item(id: str, balance: str):
    # This function overwrites the json file and the data in our API according to the ID we specified and changes the balance. We specify ID and balance in our API in the docs
    for i in range(len(data_read)):
        if id == data_read[i]["id"]: 
            data_read[i]["current_balance"] = balance 
            if data_read[i]["current_balance"] == balance: 
                with open("data.json", "w", encoding="UTF-8") as data: 
                        json.dump(data_read, data, indent=4) 
                return  data_read[i]