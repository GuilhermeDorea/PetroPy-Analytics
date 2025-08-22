'''API Functions for handle the analytics requests'''
from flask import Flask, jsonify, request

app = Flask(__name__)

precos = [
    {
        'id': 1,
        'estado':'Lavar a louça',
        'gasolina': 5,
        'gasolina aditivada': 10.3,
        'DIESEL S10': 3.1,
        'etanol': 2.5,
        'GNV' : 10
    }
]
