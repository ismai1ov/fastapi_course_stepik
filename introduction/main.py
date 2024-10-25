from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title = "Web App")


@app.get("/")
async def intro():
    return FileResponse(r'C:\Users\Vugar\Desktop\programming\fastapi_stepik\index.html')


@app.post("/calculate/{num1}/{num2}")
async def calculate(num1: int, num2: int):
    return {"status": 200,
            "result": num1 + num2}