<<<<<<< HEAD
# Supermarket Inventory Management & Analytics System

An intelligent data management and analytics application built in Python, designed to satisfy the requirements of the Python Programming Assignment.

---

## 📌 Project Overview
The **Supermarket Inventory Management System** automates product record handling, validates inventory data integrity, and delivers actionable analytical insights for procurement and stock monitoring. The system incorporates Object-Oriented Programming (OOP) principles, custom algorithms with Big-O complexity analysis, Matplotlib visual dashboards, automated reporting, and a persistent audit log[cite: 1].

---

## 👥 Group Division & Responsibilities
This project is developed collaboratively by 3 team members with modular responsibilities[cite: 1]:

* **Member 1 (`hills-crypto`) - Core Architecture, Security & Data Validation**:
  * Base class `User` and polymorphic roles (`AdminUser`, `CashierUser`)[cite: 1].
  * SHA-256 salted password hashing and role-based access control (RBAC)[cite: 1].
  * `Product` entity model and multi-rule input validation (`validate_product_data`)[cite: 1].

* **Member 2 - Custom Algorithms & Computational Complexity**:
  * **Algorithm 1 (Bubble Sort)**: In-place sorting by price, stock, or reorder level ($\mathcal{O}(N^2)$)[cite: 1].
  * **Algorithm 2 (Reorder Priority Scoring)**: Stock urgency calculation ($\mathcal{O}(1)$)[cite: 1].
  * **Algorithm 3 (Duplicate Item Detection)**: Demographic name-collision scanner ($\mathcal{O}(N^2)$)[cite: 1].
  * Linear search helper function[cite: 1].

* **Member 3 - Visual Analytics, Reporting & System Orchestration**:
  * Multi-panel Matplotlib charts (Category volume bar chart & stock health pie chart)[cite: 1].
  * Automated CSV summary report exporter (`export_report_to_csv`)[cite: 1].
  * Activity logging via Python's `logging` module to `system_activity.log`[cite: 1].
  * Interactive CLI menu integration in `main.py`[cite: 1].

---

## 🛠️ System Requirements & Architecture
* **Language**: Python 3.x[cite: 1]
* **Key Dependencies**: `matplotlib`[cite: 1], `hashlib`[cite: 1], `csv`[cite: 1], `logging`[cite: 1]
* **Dataset**: Synthetically generated benchmark dataset containing 500+ realistic product records (`supermarket_500.csv`)[cite: 1].

### Modular File Structure
```text
supermarket_system/
│
├── auth_and_data.py          # Member 1: OOP Classes, Security & Validation Rules
├── algorithms.py             # Member 2: The 3 Custom Algorithms & Search Logic
├── analytics_and_report.py   # Member 3: Matplotlib Visualizations, Logging & CSV Export
├── main.py                   # Member 3: Central Integration & Interactive CLI Menu
├── supermarket_500.csv       # Benchmark Dataset (>= 500 records)
├── system_activity.log       # System Audit Event Log
└── README.md                 # Project Documentation
=======
# Supermarket-Inventory-Management-System-collaraboration
An Intelligent Supermarket Inventory Management and Analytics System in Python demonstrating OOP, custom algorithms, validation rules, Matplotlib analytics, and automated reporting.
>>>>>>> 825cf6db27858d1ca1e60c09ac81174cb3913310
