from fastapi import FastAPI

app = FastAPI()

# decorator to -> use the app created
#"/" stands for base or homepage url
@app.get('/')
def index():
    return 'heyy'

@app.get('/about')
def about():
    return {"data": "about page"}