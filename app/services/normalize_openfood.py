import uuid

def normalize_category(categories: str) -> str:
    categories = categories.lower()
    if "wine" in categories:
        return "Wine"
    elif "beer" in categories:
        return "Beer"
    elif "spirit" in categories or "whisky" in categories or "vodka" in categories:
        return "Spirit"
    return "Other"

def parse_openfood_product(product: dict) -> dict:
    return {
        "id": str(uuid.uuid4()),
        "name": product.get("product_name", "Unnamed"),
        "category": normalize_category(product.get("categories", "")),
        "abv": float(product.get("abv", 0)),
        "price": 1000.0,  # Default or randomized
        "image": product.get("image_url", ""),
        "description": product.get("brands", "")
    }
