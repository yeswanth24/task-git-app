import random
from config import app

@app.get('/message')
def greetnow():
    return "welcome to my web page"

@app.get('/number')
def num():
    num=random.randint(0,9)
    return f"Random num {num}"