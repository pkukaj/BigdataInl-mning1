import redis
import random
import json

# Connect to Redis
db = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Get all quote keys
keys = db.keys("quote:*")

# Select a random quote key
random_key = random.choice(keys)

# Retrieve and print the quote
quote = json.loads(db.get(random_key))
print(f"{quote['quote']} - {quote['author']}")
