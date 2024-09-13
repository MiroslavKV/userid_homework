from fastapi import FastAPI
from fastapi import status, HTTPException, Query
import uvicorn

app = FastAPI(debug=True)

users = [
    {"name": "Myroslav", "age": 13, "work": "student"},
    {"name": "name", "age": 14, "work": "nothing"}
]

@app.get("/users")
def get_users():
    return users

@app.post("/users", status_code=status.HTTP_201_CREATED)
def add_user(name: str, age: int, work: str):
    users_name = [i["name"] for i in users]
    if name in users_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {name} is exists")

    users.append({"name": name, "age": age, "work": work})
    return {"name": name, "age": age, "work": work}


@app.get("/users/{id_}")
def user_by_id(id_: int):
    if id_ > len(users) - 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User not exists")
    return users[id_]


@app.delete("/users", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(name: str):
    users_name = [i["name"] for i in users]
    if name not in users_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User {name} not exists")
    id_ = users_name.index(name)
    users.pop(id_)
    return {"mess": f"{name} deleted"}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)