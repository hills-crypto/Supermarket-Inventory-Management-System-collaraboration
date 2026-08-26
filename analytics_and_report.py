"""
Member 3: Visual Analytics, CSV Reporting & Logging Subsystem
"""
import csv
import logging
import matplotlib.pyplot as plt
from algorithms import calculate_reorder_priority

# --- Simple Logging Setup ---
logging.basicConfig(
    filename="system_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message):
    """Writes an event message to system_activity.log."""
    logging.info(message)


# --- Visual Analytics (Matplotlib) ---
def show_analytics_charts(products):
    """Displays a two-panel Matplotlib dashboard showing inventory metrics."""
    if not products:
        print("No products available to display.")
        return

    # 1. Count items grouped by category
    category_counts = {}
    for p in products:
        if p.category in category_counts:
            category_counts[p.category] += 1
        else:
            category_counts[p.category] = 1

    # 2. Count low stock vs healthy stock
    low_stock_count = sum(1 for p in products if p.stock < p.min_reorder)
    healthy_stock_count = len(products) - low_stock_count

    # Create two visual panels
    plt.figure(figsize=(11, 5))

    # Panel 1: Bar Chart of Category Distribution
    plt.subplot(1, 2, 1)
    plt.bar(list(category_counts.keys()), list(category_counts.values()), color="skyblue", edgecolor="black")
    plt.title("Products per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Items")
    plt.xticks(rotation=25)

    # Panel 2: Pie Chart of Inventory Stock Health
    plt.subplot(1, 2, 2)
    labels = [f"Low Stock ({low_stock_count})", f"Healthy Stock ({healthy_stock_count})"]
    plt.pie([low_stock_count, healthy_stock_count], labels=labels, colors=["salmon", "lightgreen"], autopct="%1.1f%%", startangle=90)
    plt.title("Inventory Stock Status")

    plt.tight_layout()
    plt.show()


# --- Summary Report Generation ---
def export_report_to_csv(products, filename="inventory_report.csv"):
    """Exports full product details and computed priority scores to a CSV report."""
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Product ID", "Name", "Category", "Price", "Stock", "Min Reorder", "Reorder Priority Score"])
            for p in products:
                priority = calculate_reorder_priority(p)
                writer.writerow([p.product_id, p.name, p.category, f"${p.price:.2f}", p.stock, p.min_reorder, priority])
        print(f"\nReport successfully saved to {filename}")
        log_event(f"Exported inventory report to {filename}")
    except Exception as e:
        print(f"Error exporting report: {e}")