"""
Supermarket Inventory Management & Analytics System
Main Application Entrypoint & CLI Menu
"""
import csv
import os
import random

from auth_and_data import AdminUser, CashierUser, Product, validate_product_data
from algorithms import bubble_sort_products, calculate_reorder_priority, find_duplicate_products, search_products
from analytics_and_report import export_report_to_csv, log_event, show_analytics_charts

# Generate 500+ records automatically on first run
def generate_sample_dataset_if_missing(filename="supermarket_500.csv"):
    if os.path.exists(filename):
        return

    categories = ["Beverages", "Bakery", "Dairy", "Produce", "Meat", "Canned Goods", "Personal Care", "Cleaning"]
    items = ["Milk", "Bread", "Rice", "Apples", "Soap", "Sugar", "Cooking Oil", "Juice", "Chicken", "Biscuits", "Salt", "Flour"]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id", "name", "category", "price", "stock", "min_reorder"])
        for i in range(1, 505):
            pid = f"PRD-{1000 + i}"
            name = f"{random.choice(items)} Brand-{random.randint(1, 50)}"
            cat = random.choice(categories)
            price = round(random.uniform(1.50, 45.00), 2)
            stock = random.randint(0, 100)
            min_reorder = random.randint(10, 30)
            writer.writerow([pid, name, cat, price, stock, min_reorder])
    print(f"Generated sample dataset with 504 items: {filename}")


# Load CSV into Product objects
def load_products_from_csv(filename="supermarket_500.csv"):
    products = []
    if not os.path.exists(filename):
        return products

    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            is_valid, _ = validate_product_data(
                row["product_id"], row["name"], row["category"],
                row["price"], row["stock"], row["min_reorder"]
            )
            if is_valid:
                products.append(Product(
                    row["product_id"], row["name"], row["category"],
                    row["price"], row["stock"], row["min_reorder"]
                ))
    return products


def main():
    generate_sample_dataset_if_missing()
    products = load_products_from_csv()

    # Pre-configured system users
    users = {
        "admin": AdminUser("admin", "admin123"),
        "cashier": CashierUser("cashier", "cash123")
    }

    print("=" * 45)
    print(" Supermarket Inventory Analytics System ")
    print("=" * 45)

    # Authentication Loop
    current_user = None
    while not current_user:
        u = input("Username (admin / cashier): ").strip()
        p = input("Password (admin123 / cash123): ").strip()
        if u in users and users[u].check_password(p):
            current_user = users[u]
            print(f"\nWelcome, {current_user.username}! Role: {current_user.role}")
            log_event(f"User {current_user.username} logged in successfully.")
        else:
            print("Invalid credentials. Try again.\n")

    # Main Interactive Menu
    while True:
        print("\n--- Main Menu ---")
        print("1. View Products (First 10)")
        print("2. Search Product")
        print("3. Add New Product (Admin Only)")
        print("4. Sort Products using Bubble Sort (Member 2)")
        print("5. View Reorder Priority Alerts (Member 2)")
        print("6. Check for Duplicate Items (Member 2)")
        print("7. View Analytics Dashboard (Member 3)")
        print("8. Export Inventory CSV Report (Member 3)")
        print("9. Logout and Exit")

        choice = input("\nChoose an option (1-9): ").strip()

        if choice == "1":
            print(f"\nTotal Products Loaded: {len(products)}")
            for p in products[:10]:
                print(p.display())

        elif choice == "2":
            term = input("Enter search term (name/ID/category): ").strip()
            results = search_products(products, term)
            print(f"\nFound {len(results)} matches:")
            for r in results[:10]:
                print(r.display())

        elif choice == "3":
            if current_user.role != "Admin":
                print("Access Denied: Only Admins can add products.")
                continue

            pid = input("Product ID (e.g., PRD-9999): ").strip()
            name = input("Product Name: ").strip()
            cat = input("Category: ").strip()
            price = input("Price: ").strip()
            stock = input("Stock Quantity: ").strip()
            min_r = input("Minimum Reorder Level: ").strip()

            is_valid, msg = validate_product_data(pid, name, cat, price, stock, min_r)
            if is_valid:
                new_prod = Product(pid, name, cat, price, stock, min_r)
                products.append(new_prod)
                print("Product added successfully!")
                log_event(f"Admin added product {pid}")
            else:
                print(f"Failed to add: {msg}")

        elif choice == "4":
            field = input("Sort by (price / stock / min_reorder): ").strip()
            if field not in ["price", "stock", "min_reorder"]:
                print("Invalid field name.")
                continue
            desc = input("Sort descending? (y/n): ").strip().lower() == "y"
            sorted_list = bubble_sort_products(products, sort_by=field, descending=desc)
            print(f"\n--- Top 10 Sorted by {field} ---")
            for p in sorted_list[:10]:
                print(p.display())

        elif choice == "5":
            alerts = []
            for p in products:
                score = calculate_reorder_priority(p)
                if score > 0:
                    alerts.append((p, score))
            alerts.sort(key=lambda x: x[1], reverse=True)
            print(f"\n--- Top 10 Items Needing Restock ---")
            for p, score in alerts[:10]:
                print(f"URGENCY SCORE: {score:>2} | {p.display()}")

        elif choice == "6":
            dups = find_duplicate_products(products)
            print(f"\nFound {len(dups)} pairs of matching names:")
            for p1, p2 in dups[:5]:
                print(f"Match: [{p1.product_id}] {p1.name} <==> [{p2.product_id}] {p2.name}")

        elif choice == "7":
            show_analytics_charts(products)

        elif choice == "8":
            export_report_to_csv(products)

        elif choice == "9":
            print("Session ended. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-9.")


if __name__ == "__main__":
    main()