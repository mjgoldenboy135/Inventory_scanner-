import json

# Load database
with open("products.json", "r") as f:
    db = json.load(f)

def get_product(gtin):
    if gtin in db:
        return db[gtin]
    else:
        return "❌ Product not found"

# User input
gtin = input("📷 Scan or enter GTIN: ")

# Output
product = get_product(gtin)
print("🧾 Product Name:", product)
