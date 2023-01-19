from fastapi import FastAPI, HTTPException, Request, Response
from typing import Dict

app = FastAPI()

@app.post("/calculate/")
async def calculate(request: Request) -> Dict[str, float]:
    try:
        data = await request.json()
        operator = data["operator"]
        num1 = data["num1"]
        num2 = data["num2"]

        if operator == "add":
            result = num1 + num2
        elif operator == "subtract":
            result = num1 - num2
        elif operator == "multiply":
            result = num1 * num2
        elif operator == "divide":
            result = num1 / num2
        else:
            raise HTTPException(status_code=400, detail="Invalid operator")
        
        return {"result": result}
    except:
        raise HTTPException(status_code=400, detail="Invalid input")
