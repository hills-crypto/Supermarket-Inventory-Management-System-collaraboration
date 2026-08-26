import hashlib

# --- OOP: Base Class (Encapsulation & Inheritance) ---
class User:
    def __init__(self, username, password, role):
        self.username = username
        # Encapsulation: Store hashed password rather than plain text
        self.password_hash = self.hash_password(password)
        self.role = role

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == self.hash_password(password)

    def get_role_description(self):
        return "Generic System User"


# --- OOP: Subclasses (Polymorphism) ---
class AdminUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="Admin")

    def get_role_description(self):
        return "Administrator with full system access"


class CashierUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="Cashier")

    def get_role_description(self):
        return "Cashier with view and search access only"


# --- OOP: Product Record Class ---
class Product:
    def __init__(self, product_id, name, category, price, stock, min_reorder):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)
        self.min_reorder = int(min_reorder)

    def display(self):
        return f"ID: {self.product_id} | Name: {self.name:<18} | Cat: {self.category:<12} | Price: ${self.price:>6.2f} | Stock: {self.stock:>4} | Min: {self.min_reorder}"


# --- Data Validation Rules ---
def validate_product_data(product_id, name, category, price, stock, min_reorder):
    # Rule 1: No empty strings
    if not product_id.strip() or not name.strip() or not category.strip():
        return False, "Error: Product ID, Name, and Category cannot be empty."

    # Rule 2: Price must be positive
    try:
        p = float(price)
        if p <= 0:
            return False, "Validation Rule 1 Failed: Price must be greater than 0."
    except ValueError:
        return False, "Error: Price must be a valid number."

    # Rule 3: Stock cannot be negative
    try:
        s = int(stock)
        if s < 0:
            return False, "Validation Rule 2 Failed: Stock cannot be negative."
    except ValueError:
        return False, "Error: Stock must be an integer."

    # Rule 4: Minimum reorder level must be positive
    try:
        m = int(min_reorder)
        if m < 0:
            return False, "Validation Rule 3 Failed: Minimum reorder level cannot be negative."
    except ValueError:
        return False, "Error: Minimum reorder level must be an integer."

    return True, "Valid"