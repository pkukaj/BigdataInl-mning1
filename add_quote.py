import redis
import json

# Connect to Redis
db = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Input for a new quote
quote_text = input("Enter the quote: ")
author = input("Enter the author: ")

# Generate a new ID (not optimized, just for demo)
new_id = max([int(key.split(b':')[1]) for key in db.keys("quote:*")]) + 1

# Store the new quote
db.set(f"quote:{new_id}", json.dumps({"id": new_id, "quote": quote_text, "author": author}))

print("New quote added to the Redis database.")
