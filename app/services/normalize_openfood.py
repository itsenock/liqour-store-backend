import uuid

def normalize_category(categories: str) -> str:
    categories = categories.lower()
    if "wine" in categories:
        return "Wine"
    elif "beer" in categories:
        return "Beer"
    elif any(x in categories for x in ["spirit", "whisky", "vodka", "rum", "gin"]):
        return "Spirit"
    return "Other"

def parse_openfood_product(product: dict) -> dict:
    try:
        abv_raw = product.get("abv", 0)
        abv = float(abv_raw) if abv_raw not in [None, ""] else 0.0

        category = normalize_category(product.get("categories", ""))
        subcategory = product.get("categories_tags", ["Other"])
        subcategory = subcategory[0].split(":")[-1].capitalize() if subcategory else "Other"

        return {
            "id": str(uuid.uuid4()),
            "name": product.get("product_name", "Unnamed").strip(),
            "category": category,
            "subcategory": subcategory or "Other",  # ✅ fallback
            "abv": abv,
            "price": 1000.0,
            "image": product.get("image_url", ""),
            "description": product.get("brands", "").strip()
        }
    except Exception as e:
        print(f"Failed to parse product: {e}")
        return {}
