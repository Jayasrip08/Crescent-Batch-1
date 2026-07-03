# ============================================================
# DEMO 1 — Functions: beyond the basics
# Live-code this. Students already know def/return from Day 1-2 warmups.
# ============================================================

# Refresher: parameters + return
def add(a, b):
    return a + b

print(add(4, 5))  # 9

# LEVEL UP 1 — Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Afsin"))                  # Hello, Afsin!
print(greet("Afsin", "Welcome back"))  # Welcome back, Afsin!

# LEVEL UP 2 — Keyword arguments (order stops mattering)
def describe_transaction(amount, txn_type, note=""):
    return f"[{txn_type.upper()}] amount={amount} note={note}"

print(describe_transaction(txn_type="deposit", amount=500, note="salary"))

# LEVEL UP 3 — Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([40, 10, 90, 25])
print(f"low={low} high={high}")

# LEVEL UP 4 — *args: accept ANY number of positional arguments
def total_deposits(*amounts):
    return sum(amounts)

print(total_deposits(100, 200, 50))       # 350
print(total_deposits(100, 200, 50, 75))   # 425 -- works with any count

# LEVEL UP 5 — **kwargs: accept ANY number of named arguments
def build_receipt(**details):
    lines = [f"{key}: {value}" for key, value in details.items()]
    return "\n".join(lines)

print(build_receipt(customer="Afsin", amount=500, type="Deposit"))
