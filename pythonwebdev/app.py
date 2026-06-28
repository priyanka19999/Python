from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get('/')
def home():
    return{'data':'welcome to home page'}

@app.get('/contact')
def contact():
    return{'data':'welcome to contact page'}


@app.get('/about')
def about():
    return{'data':'welcome to about page'}


@app.post('/upload')
def upload_image(files: list[UploadFile] ):
    print(files)
    return{'status':'file Uploaded successfully'}

import uvicorn
uvicorn.run(app)