from fastapi import FastAPI
from database import Base, engine
from router.auth import router
from router.income import income_router
app = FastAPI()


app.include_router(router)
app.include_router(income_router)

@app.get("/")
def home():
    return {
        "msg" : "hello world"
    }




Base.metadata.create_all(engine)