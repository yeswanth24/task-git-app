from config import app
import random

@app.get('/message')
def greetnow():
    return "welcome to my web page"

@app.get('/number')
def num():
    return random.randint(0,9)