from fastapi import FastAPI

# creating an instance of app (u will use this while running (i.e, instance))
app = FastAPI()

# decorator to -> use the app created
#"(/)" stands for "Path" (and only slast path is for base or homepage url)
# "get" refers to the "Operation" on the path
@app.get('/')
# decorator is also called 'Path Operation Decorator'
# below function is named as: 'PATH OPERATION FUNCTION'
def index():
    return 'heyy'

@app.get('/about')
def about():
    return {"data": "about page"}