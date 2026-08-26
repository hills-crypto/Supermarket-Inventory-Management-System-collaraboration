"""
Member 2: Custom Algorithms & Complexity Module
- Algorithm 1: Bubble Sort (Sorting)
- Algorithm 2: Reorder Priority Calculation (Priority Scoring)
- Algorithm 3: Duplicate Item Detection (Duplicate Checking)
"""

# =====================================================================
# ALGORITHM 1: Bubble Sort
# Time Complexity: O(N^2) average/worst | Space Complexity: O(1)
# =====================================================================
def bubble_sort_products(products, sort_by="price", descending=False):
    """Sorts a list of Product objects using the Bubble Sort algorithm."""
    items = list(products)
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = getattr(items[j], sort_by)
            val2 = getattr(items[j + 1], sort_by)

            should_swap = (val1 < val2) if descending else (val1 > val2)
            if should_swap:
                # Swap neighboring items
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


# =====================================================================
# ALGORITHM 2: Reorder Priority Scoring
# Time Complexity: O(1) per product | Space Complexity: O(1)
# =====================================================================
def calculate_reorder_priority(product):
    """
    Calculates restock urgency.
    If stock is below the minimum reorder level, score > 0.
    The larger the shortage, the higher the emergency score.
    """
    if product.stock < product.min_reorder:
        shortage = product.min_reorder - product.stock
        score = shortage * 2
    else:
        score = 0
    return score


# =====================================================================
# ALGORITHM 3: Duplicate Item Detection
# Time Complexity: O(N^2) | Space Complexity: O(K) duplicates found
# =====================================================================
def find_duplicate_products(products):
    """Scans all products to find identical/conflicting product names."""
    duplicates = []
    n = len(products)

    for i in range(n):
        for j in range(i + 1, n):
            name1 = products[i].name.lower().strip()
            name2 = products[j].name.lower().strip()
            if name1 == name2:
                duplicates.append((products[i], products[j]))

    return duplicates


# Linear Search Helper
def search_products(products, search_term):
    """Performs case-insensitive search across name, ID, and category."""
    term = search_term.lower()
    results = []
    for item in products:
        if term in item.name.lower() or term in item.product_id.lower() or term in item.category.lower():
            results.append(item)
    return results