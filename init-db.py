import redis
import json

# Connect to Redis
db = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Example quotes
quotes = [
    {"id": 1, "quote": "Your heart is the size of an ocean. Go find yourself in its hidden depths.", "author": "Rumi"},
    # Add more quotes as needed...
]

# Store each quote in Redis
for quote in quotes:
    db.set(f"quote:{quote['id']}", json.dumps(quote))

print("Quotes initialized in the Redis database.")
