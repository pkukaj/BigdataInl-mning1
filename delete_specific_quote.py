import redis
import json

# Definiera det specifika citatet och författaren du vill radera
target_quote = "Att våga är att förlora fotfästet en stund. Att inte våga är att förlora sig själv."
target_author = "Sören Kierkegaard"

# Anslut till Redis-databasen
db = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Iterera över alla citat och leta efter matchningen
deleted = False
for key in db.keys("quote:*"):
    quote_data = json.loads(db.get(key))
    if quote_data["quote"] == target_quote and quote_data["author"] == target_author:
        db.delete(key)
        deleted = True
        print(f"Deleted the quote: '{target_quote}' by {target_author}")
        break

if not deleted:
    print("Quote not found.")
