from time import time

PORT = 5000
HOST = '0.0.0.0'
FIRST_BLOCK = {
    "index": 1,
    "timestamp": time(),
    "transactions": [],
    "proof": 1,
    "previous_hash": "0"
}