from http.client import HTTPException
from fastapi import FastAPI
from fastapi import status
import uvicorn

app = FastAPI(debug=True)

users = {
    "Myroslav": {"age": 13, "work": "student"},
    "name": {"age": 14, "work": "nothing"}
}

@app.get("/users")
def get_users():
    return users

@app.post("/users", status_code=status.HTTP_201_CREATED)
def add_user(name: str, age: int, work: str):
    if name in users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {name} already exists")

    users[name] = {"age": age, "work": work}
    return {"name": name, "age": age, "work": work}

@app.get("/users/{name}")
def user_by_name(name: str):
    if name not in users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {name} does not exist")
    return {name: users[name]}

@app.delete("/users", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(name: str):
    if name not in users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {name} does not exist")

    del users[name]
    return {"message": f"User {name} deleted"}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)