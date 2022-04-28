from config import app
import random

@app.get('/message')
def greetnow():
    return "welcome to my web page"

@app.get('/number')
def fun():
    return random.randint(0,9) :" This is a sample page"