from flask import Flask, jsonify
from dice_roller.dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    return jsonify({'roll': dice.roll()})
