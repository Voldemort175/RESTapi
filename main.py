from fastapi import FastAPI
import statistics
app = FastAPI()

numbers = []

@app.post("/numbers")
async def addNumber(new):
    if new.isdigit() == True:
         numbers.append(int(new))
         return {"result": "OK"}
    else:
        return {"result": "Error"}
    
        

@app.get("/numbers/average")
async def getAvg():
    if (numbers == []):
        return {"result": "No numbers in the array"}
    else:
        avg = sum(numbers) / len(numbers)
        return {"result": avg }

@app.get("/numbers/sum")
async def getSum():
    if (numbers == []):
        return {"result": "No numbers in the array"}
    else:
        sum1 = sum(numbers)
        return {"result": sum1 }

@app.get("/numbers/stddev")
async def getStdev():
    if (numbers == []):
        return {"result": "No numbers in the array"}
    else:
        stddev = statistics.stdev(numbers)
        return {"result": stddev }      

@app.get("/numbers/show")
async def show():
    return {"result": numbers }
