import uvicorn
import score
from fastapi import FastAPI
from tdp_input import TDPInputs

# start app
app = FastAPI()


# render default webpage
@app.get('/')
def home():
    return {'message': 'Hello world! This is Fast API app default page'}


# predict demand
@app.post('/predict')
def get_data(data: TDPInputs):
    data = data.dict()
    return {"demand percent is ": score.run(data)}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn fastAPI_app:app --reload
